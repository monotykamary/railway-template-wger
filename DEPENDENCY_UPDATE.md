## Dependency and secure-cookie candidate — 2026-11-16

Update the digest-pinned Caddy adapter from 2.11.7 to stable 2.11.9. Keep wger 2.7.0 and PostgreSQL 17.11 unchanged with their exact image digests.

The owned-TLS preflight found a session cookie without its Secure flag. Preserve the pinned image's original `settings/main.py` verbatim and append only `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`. The Docker build verifies the original upstream file hash before installing this AGPL-licensed adaptation. Do not work around this by replaying cookies over HTTP or weakening the client guard.

Validation must use HTTPS to load the real UI/static asset, reject wrong credentials and unauthorized writes, verify actual secure session/CSRF cookies, create a workout routine and training day through the authenticated API, and retrieve the exact original records after upgrade and redeploy without reseeding. Full boat and live Railway product/persistence gates remain mandatory. This branch is a candidate, not a released template.
