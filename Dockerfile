FROM docker.io/library/caddy:2.11.7-alpine@sha256:d8542f48d34a9cf4e4c11a478865229840e87e4c96ea3f439101f31a5d35f75f AS caddy
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
