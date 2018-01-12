#!/usr/bin/env bash

set -ex

cd /usr/bin/
exec uwsgi --http 0.0.0.0:34000 -p 1 -w entrypoint --enable-threads
