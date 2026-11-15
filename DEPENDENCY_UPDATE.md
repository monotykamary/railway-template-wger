## Dependency candidate — 2026-11-15

Update only the digest-pinned Caddy adapter binary from 2.11.7 to stable 2.11.9. Keep wger 2.7.0 and its database unchanged, with exact existing image digests. Every production FROM remains version/digest-pinned. Official Caddy release notes and manifest/platform evidence are retained in release artifacts.

Validation must load the real web UI/static asset, reject a wrong administrator password and unauthorized workout creation, create a workout routine and training day through the authenticated API, and retrieve both exact records after upgrade and redeploy without reseeding. Secure cookies are replayed explicitly only inside the worker-local HTTP fixture; production secure-cookie settings and HTTPS proxy headers are unchanged. Full live Railway HTTPS/product gates remain mandatory.
