# wger on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/wger?referralCode=ZqgrJ0)

Deploy wger 2.7.0 with generated administrator and session secrets, persistent JWT keys and media, private Postgres, and daily backups. Caddy serves static and media files in the same service, avoiding unsafe shared volumes.

Sign in as `admin` with `WGER_ADMIN_PASSWORD`. Public registration and guest accounts are disabled by default. Use one application replica because media uses an attached volume.

Use the public Railway **HTTPS** URL for sign-in. Session and CSRF cookies are explicitly marked `Secure`; authenticated browser sessions are not supported over plaintext HTTP. Caddy forwards the trusted HTTPS scheme to the loopback-only application server.

Upstream: https://github.com/wger-project/wger/tree/2.7 (AGPL-3.0-or-later). Not affiliated with Railway.
