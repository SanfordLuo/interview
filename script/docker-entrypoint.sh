#!/bin/bash
set -Eeuo pipefail

# wait network ready
sleep 3s

# allow the container to be started with `--user`
# uwsgi command should be dropped to the correct user
if [ "$1" = 'uwsgi' -a "$(id -u)" = '0' ]; then
	find . \! -user app -exec chown app '{}' +
	exec gosu app "$BASH_SOURCE" "$@"
fi

exec "$@"
