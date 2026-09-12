# Infrastructure Reference

## AWS Architecture

```
Internet → Route 53 → CloudFront (static) / ALB (dynamic)
                              ↓
                         EC2 (NestJS via PM2 + Nginx)
                              ↓
                    RDS (PostgreSQL) + S3 (files)
```

**Service mapping:**
| Service | Usage |
|---------|-------|
| EC2 | NestJS backend runtime |
| RDS | PostgreSQL (production DB) |
| S3 | File uploads, static assets |
| CloudFront | CDN for S3 + Next.js static |
| Lambda | Isolated serverless tasks only (cron jobs, webhooks, one-off triggers) — not part of core backend |
| Cognito | User pool, token issuance |
| API Gateway | Lambda HTTP trigger (when Lambda is used) |

---

## Nginx Config (NestJS on EC2)

```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;      # WebSocket support
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_cache_bypass $http_upgrade;
    }
}
```

For HTTPS, use Certbot: `certbot --nginx -d api.yourdomain.com`

---

## PM2 Ecosystem

```javascript
// ecosystem.config.js (in backend/)
module.exports = {
  apps: [{
    name: 'api',
    script: 'dist/main.js',
    instances: 'max',        // cluster mode — one per CPU core
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'production',
      PORT: 3001,
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    merge_logs: true,
  }],
};
```

**Deploy commands:**
```bash
npm run build
pm2 startOrRestart ecosystem.config.js --env production
pm2 save
```

---

## GitHub Actions CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install & Build
        working-directory: backend
        run: |
          npm ci
          npm run build

      - name: Deploy to EC2
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_SSH_KEY }}
          script: |
            cd /app/backend
            git pull origin main
            npm ci --omit=dev
            npm run build
            npx prisma migrate deploy
            pm2 restart ecosystem.config.js --env production

  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          working-directory: frontend
          vercel-args: '--prod'
```

**Required GitHub Secrets:**
- `EC2_HOST`, `EC2_SSH_KEY`
- `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`

---

## S3 File Upload Pattern

```typescript
// backend: use AWS SDK v3
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

// Generate presigned URL → frontend uploads directly to S3 (no backend bottleneck)
async getUploadUrl(key: string, contentType: string) {
  const command = new PutObjectCommand({
    Bucket: process.env.AWS_S3_BUCKET,
    Key: key,
    ContentType: contentType,
  });
  return getSignedUrl(this.s3, command, { expiresIn: 300 });
}
```

Frontend calls `GET /api/v1/upload-url`, gets presigned URL, PUTs file directly.

---

## Deployment Checklist

- [ ] `prisma migrate deploy` run before app restart
- [ ] `.env` updated on EC2
- [ ] PM2 restarted with `startOrRestart` (not `start`)
- [ ] Nginx config reloaded if changed: `nginx -s reload`
- [ ] S3 bucket CORS configured for frontend domain
- [ ] Cognito callback URLs updated for new domain
