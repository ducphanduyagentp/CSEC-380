FROM fbraz3/lnmp

COPY ./armbook/ /app/public/
COPY run.sh /
RUN chmod +x /run.sh

EXPOSE 80

CMD ["/run.sh"]
