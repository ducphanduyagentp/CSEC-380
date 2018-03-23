FROM fbraz3/lnmp

#COPY ./armbook/ /app/public/
COPY nginx.* /etc/nginx/
COPY default.conf /etc/nginx/sites-enabled/default
COPY run.sh /
RUN chmod +x /run.sh

EXPOSE 80 443

CMD ["/run.sh"]
