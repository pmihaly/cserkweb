FROM nginx:1.17.4-alpine

# Kontextus a projekt gyökérmappája (nem az nginx mappa)

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY static/ /usr/src/app/static
COPY media/ /usr/src/app/media