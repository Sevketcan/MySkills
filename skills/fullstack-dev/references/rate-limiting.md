# Rate Limiting

Use `@nestjs/throttler` in every project. Set up globally, override per endpoint where needed.

---

## Installation

```bash
npm install @nestjs/throttler
```

---

## Global Setup

```typescript
// app.module.ts
import { ThrottlerModule, ThrottlerGuard } from '@nestjs/throttler';
import { APP_GUARD } from '@nestjs/core';

@Module({
  imports: [
    ThrottlerModule.forRoot([
      {
        name: 'default',
        ttl: 60_000,   // 1 minute window
        limit: 60,     // 60 requests per window (default)
      },
    ]),
  ],
  providers: [
    {
      provide: APP_GUARD,
      useClass: ThrottlerGuard,  // applied globally to all routes
    },
  ],
})
export class AppModule {}
```

---

## Per-Endpoint Overrides

```typescript
import { Throttle, SkipThrottle } from '@nestjs/throttler';

// Stricter limit for auth endpoints
@Controller('auth')
export class AuthController {

  @Post('login')
  @Throttle({ default: { ttl: 60_000, limit: 5 } })  // 5 attempts per minute
  login(@Body() dto: LoginDto) {}

  @Post('register')
  @Throttle({ default: { ttl: 60_000, limit: 3 } })  // 3 per minute
  register(@Body() dto: RegisterDto) {}
}

// Skip throttle for internal/health endpoints
@Controller('health')
@SkipThrottle()
export class HealthController {
  @Get() check() { return { status: 'ok' }; }
}
```

---

## Recommended Limits Per Endpoint Type

| Endpoint Type | TTL | Limit |
|---|---|---|
| Default (all routes) | 60s | 60 |
| Auth — login | 60s | 5 |
| Auth — register | 60s | 3 |
| Auth — forgot password | 60s | 3 |
| File upload | 60s | 10 |
| Public API (no auth) | 60s | 30 |
| WebSocket connection | — | handled separately |

---

## Custom Error Response

Override the default throttler exception for a consistent response shape:

```typescript
// common/filters/throttler-exception.filter.ts
import { ExceptionFilter, Catch, ArgumentsHost, HttpStatus } from '@nestjs/common';
import { ThrottlerException } from '@nestjs/throttler';

@Catch(ThrottlerException)
export class ThrottlerExceptionFilter implements ExceptionFilter {
  catch(exception: ThrottlerException, host: ArgumentsHost) {
    const response = host.switchToHttp().getResponse();
    response.status(HttpStatus.TOO_MANY_REQUESTS).json({
      statusCode: 429,
      message: 'Too many requests. Please slow down.',
      data: null,
    });
  }
}
```

Register in `main.ts`:

```typescript
app.useGlobalFilters(new ThrottlerExceptionFilter());
```

---

## WebSocket Rate Limiting

Throttler does not apply to WebSocket gateways automatically. Handle in `handleConnection`:

```typescript
@WebSocketGateway({ namespace: '/chat' })
export class ChatGateway implements OnGatewayConnection {
  private connectionCount = new Map<string, number>();

  handleConnection(client: Socket) {
    const ip = client.handshake.address;
    const count = this.connectionCount.get(ip) ?? 0;

    if (count >= 5) {
      client.disconnect();
      return;
    }

    this.connectionCount.set(ip, count + 1);
    client.on('disconnect', () => {
      this.connectionCount.set(ip, (this.connectionCount.get(ip) ?? 1) - 1);
    });
  }
}
```
