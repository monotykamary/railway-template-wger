#!/bin/sh
set -eu
: "${WGER_ADMIN_PASSWORD:?WGER_ADMIN_PASSWORD is required}"
mkdir -p /home/wger/media /home/wger/static
chown -R 1000:1000 /home/wger/media /home/wger/static
exec setpriv --reuid=1000 --regid=1000 --clear-groups /usr/local/bin/wger-railway-run
