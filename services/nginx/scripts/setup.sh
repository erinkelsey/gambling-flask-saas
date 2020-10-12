#!/bin/sh

certbot certonly -n -d snakeeyes.streamtechapp.com \
    --standalone --preferred-challenges http --email info@streamtechapp.com --agree-tos --expand


/usr/sbin/nginx -g "daemon off;"