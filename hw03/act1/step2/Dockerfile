FROM alpine

COPY act1step2.py my_socks.py /

RUN apk add --no-cache python && \
    python -m ensurepip && \
    pip install beautifulsoup4

CMD python /act1step1.py
