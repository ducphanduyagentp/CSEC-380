FROM alpine

COPY act2.py my_socks.py out_spiderman.py /

RUN apk add --no-cache python && \
    python -m ensurepip && \
    pip install beautifulsoup4

CMD python /act2.py
