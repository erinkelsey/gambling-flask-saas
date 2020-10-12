FROM nginx:1.17-alpine

RUN apk add --no-cache certbot

RUN mkdir /var/lib/certbot

COPY scripts/setup.sh /setup.sh
RUN chmod +x /setup.sh

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

ENTRYPOINT [ "../setup.sh" ]