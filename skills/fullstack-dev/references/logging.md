# Logging Strategy

NestJS built-in Logger for application-level logging. No external logging library by default — PM2 handles log persistence on EC2.

---

## Logger Setup

Use NestJS's built-in `Logger` — one instance per service, scoped by class name.

```typescript
// Any service
import { Injectable, Logger } from '@nestjs/common';

@Injectable()
export class ProjectsService {
  private readonly logger = new Logger(ProjectsService.name);

  async create(dto: CreateProjectDto) {
    this.logger.log(`Creating project: ${dto.name}`);
    try {
      const project = await this.prisma.project.create({ data: dto });
      this.logger.log(`Project created: ${project.id}`);
      return project;
    } catch (error) {
      this.logger.error(`Failed to create project`, error.stack);
      throw error;
    }
  }
}
```

---

## Log Levels & When to Use Each

| Level | Method | Use for |
|-------|--------|---------|
| LOG | `logger.log()` | Normal operations — created, updated, started |
| WARN | `logger.warn()` | Unexpected but recoverable — retry, fallback used, deprecated call |
| ERROR | `logger.error()` | Failures — always include `error.stack` |
| DEBUG | `logger.debug()` | Dev-only detail — query params, response shape |
| VERBOSE | `logger.verbose()` | Granular trace — disable in production |

```typescript
// main.ts — disable debug/verbose in production
const app = await NestFactory.create(AppModule, {
  logger: process.env.NODE_ENV === 'production'
    ? ['log', 'warn', 'error']
    : ['log', 'warn', 'error', 'debug'],
});
```

---

## What to Log

### ✅ Always log
- Service-level operations: entity created, updated, deleted (with ID)
- Auth events: login success, login failure, token refresh
- External API calls: outbound request + response status
- Background jobs: started, completed, failed
- Unhandled errors: always with `error.stack`

### ❌ Never log
- Passwords, tokens, secrets
- Full request bodies (may contain sensitive data)
- PII — email, phone, name in plain log lines
- DB query results (too noisy, use debug level only in dev)

---

## Global Exception Filter with Logging

```typescript
// common/filters/global-exception.filter.ts
import {
  ExceptionFilter, Catch, ArgumentsHost,
  HttpException, HttpStatus, Logger,
} from '@nestjs/common';

@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
  private readonly logger = new Logger('ExceptionFilter');

  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const request = ctx.getRequest();

    const status = exception instanceof HttpException
      ? exception.getStatus()
      : HttpStatus.INTERNAL_SERVER_ERROR;

    const message = exception instanceof HttpException
      ? exception.message
      : 'Internal server error';

    if (status >= 500) {
      this.logger.error(
        `${request.method} ${request.url} → ${status}`,
        exception instanceof Error ? exception.stack : String(exception),
      );
    } else if (status >= 400) {
      this.logger.warn(`${request.method} ${request.url} → ${status}: ${message}`);
    }

    response.status(status).json({
      statusCode: status,
      message,
      data: null,
    });
  }
}
```

Register in `main.ts`:
```typescript
app.useGlobalFilters(new GlobalExceptionFilter());
```

---

## Request Logging Interceptor

Log every incoming request in development, only slow requests (>1s) in production:

```typescript
// common/interceptors/logging.interceptor.ts
import {
  Injectable, NestInterceptor, ExecutionContext,
  CallHandler, Logger,
} from '@nestjs/common';
import { Observable, tap } from 'rxjs';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  private readonly logger = new Logger('HTTP');
  private readonly slowThreshold = 1000; // ms

  intercept(context: ExecutionContext, next: CallHandler): Observable<unknown> {
    const req = context.switchToHttp().getRequest();
    const { method, url } = req;
    const start = Date.now();

    return next.handle().pipe(
      tap(() => {
        const duration = Date.now() - start;
        const isProd = process.env.NODE_ENV === 'production';

        if (!isProd) {
          this.logger.debug(`${method} ${url} — ${duration}ms`);
        } else if (duration > this.slowThreshold) {
          this.logger.warn(`SLOW ${method} ${url} — ${duration}ms`);
        }
      }),
    );
  }
}
```

Register globally in `app.module.ts`:
```typescript
providers: [{ provide: APP_INTERCEPTOR, useClass: LoggingInterceptor }]
```

---

## PM2 Log Management (Production)

PM2 handles log file rotation on EC2. Configure in `ecosystem.config.js`:

```javascript
module.exports = {
  apps: [{
    name: 'api',
    script: 'dist/main.js',
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    merge_logs: true,
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
  }],
};
```

**Useful PM2 log commands:**
```bash
pm2 logs api           # tail all logs
pm2 logs api --err     # errors only
pm2 flush api          # clear log files
pm2 install pm2-logrotate  # auto-rotate (run once on server setup)
```

---

## Log Verbosity by Environment

| Level | Development | Production |
|-------|-------------|------------|
| log | ✅ | ✅ |
| warn | ✅ | ✅ |
| error | ✅ | ✅ |
| debug | ✅ | ❌ |
| verbose | ✅ | ❌ |
| Slow request warning (>1s) | ❌ | ✅ |
| All request logging | ✅ | ❌ |
