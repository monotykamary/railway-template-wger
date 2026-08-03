#!/bin/bash
set -euo pipefail
cd /home/wger/src
jwt=/home/wger/media/.railway-jwt.env
if [ ! -s "$jwt" ]; then
  python3 manage.py generate-jwt-keys --no-color >"$jwt"
  chmod 600 "$jwt"
fi
set -a
source "$jwt"
set +a
wger bootstrap --no-process-static
python3 manage.py collectstatic --no-input --clear
python3 manage.py migrate
python3 manage.py set-site-url
python3 manage.py shell -c "import os; from django.contrib.auth.models import User; u=User.objects.get(username='admin'); u.set_password(os.environ['WGER_ADMIN_PASSWORD']); u.email=os.environ.get('WGER_ADMIN_EMAIL','admin@example.com'); u.save()"
gunicorn wger.wsgi:application --preload --bind 127.0.0.1:8000 &
app=$!
trap 'kill -TERM "$app" 2>/dev/null || true; wait "$app"' TERM INT
caddy run --config /etc/caddy/Caddyfile --adapter caddyfile &
proxy=$!
wait -n "$app" "$proxy"
status=$?
kill -TERM "$app" "$proxy" 2>/dev/null || true
wait || true
exit "$status"
