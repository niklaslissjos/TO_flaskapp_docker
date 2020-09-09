FROM tutum/nginx

ENV STATIC_URL /static
ENV STATIC_PATH /usr/src/app/static

RUN rm /etc/nginx/sites-enabled/default

COPY sites-enabled/ /etc/nginx/sites-enabled
