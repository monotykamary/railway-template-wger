FROM docker.io/library/caddy:2.10.2-alpine@sha256:d8c17a862962def15cde69863a3a463f25a2664942eafd7bdbf050e9c3116b83 AS caddy
FROM docker.io/wger/server:2.6.0@sha256:6cf0f9a002d208fdee9abf5c20c8723b2eb34342f7673455e717a1519046e062
USER root
ENV HOME=/home/wger
COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY Caddyfile /etc/caddy/Caddyfile
COPY entrypoint.sh /usr/local/bin/wger-railway-entrypoint
COPY run.sh /usr/local/bin/wger-railway-run
RUN chmod +x /usr/local/bin/wger-railway-entrypoint /usr/local/bin/wger-railway-run
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/wger-railway-entrypoint"]
