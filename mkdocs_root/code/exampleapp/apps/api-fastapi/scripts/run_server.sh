#!/bin/sh
# run_server.sh
# Run a Chalice application with Gunicorn in a local development environment
# 2022-02-18 | CR
#
# Parameters:
# $1 = $PORT (default: 5001)
# $2 = Base dir [default: .]
#
if [ -f ".env" ] ; then
    set -o allexport; . .env ; set +o allexport ;
fi

python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt

PORT=$1
BASE_DIR=$2
if [ "$PORT" = "" ]; then
    PORT="5001"
fi
if [ "$BASE_DIR" = "" ]; then
    BASE_DIR="."
fi
# mkdir -p ${BASE_DIR}/logs ;
# touch ${BASE_DIR}/logs/app_general.log

gunicorn -b 0.0.0.0:${PORT} --log-level debug -w 4 'chalicelib.index:create_app()'

# Ports in use
# sudo lsof -PiTCP -sTCP:LISTEN