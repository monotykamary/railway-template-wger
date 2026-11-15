FROM docker.io/library/caddy:2.11.9-alpine@sha256:003a97808e781aa9f7e75cc2f43d34d461099031faf5e20faefb9f61126836f0 AS caddy
FROM docker.io/wger/server:2.7.0@sha256:a54ae2d0b59e84028a5967193b459eff6c98f44518b561f63b2e709d16b2568c
USER root
ENV HOME=/home/wger
COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY Caddyfile /etc/caddy/Caddyfile
COPY entrypoint.sh /usr/local/bin/wger-railway-entrypoint
COPY run.sh /usr/local/bin/wger-railway-run
RUN chmod +x /usr/local/bin/wger-railway-entrypoint /usr/local/bin/wger-railway-run
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/wger-railway-entrypoint"]
