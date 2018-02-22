FROM alpine

COPY act1step2.py my_socks.py /

RUN apk add --no-cache python && \
    python -m ensurepip && \
    pip install beautifulsoup4

CMD for i in {1..100}; do \
        echo "Trial $i"
        python /act1step2.py \
        echo "Done $i"
    done