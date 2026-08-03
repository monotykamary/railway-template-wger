# Deploy and Host wger on Railway

## About Hosting wger

wger is an open-source workout, exercise, nutrition, body-weight, and gym-management application. This template deploys stable 2.6.0 with generated credentials and private Postgres.

Sign in as `admin` with `WGER_ADMIN_PASSWORD`.

## Common Use Cases

- Plan workouts and track progress
- Record nutrition and body measurements
- Manage exercises and gym members

## Dependencies for wger Hosting

### Deployment Dependencies

One wger/Caddy service and private Postgres service use daily-backed-up volumes. Railway provides HTTPS.

### Implementation Details

The adapter generates and persists an RSA JWT pair, runs migrations, rotates the default bootstrap admin, and serves static/media files in-process. Registration and guest users are disabled. Use one application replica.

## Why Deploy wger on Railway?

Railway provides generated credentials, private networking, HTTPS, persistent storage, backups, health checks, and Git-driven updates.
