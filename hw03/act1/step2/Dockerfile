FROM alpine

COPY act1step2.py my_socks.py run.sh /

RUN apk add --no-cache python bash && \
    python -m ensurepip && \
    pip install beautifulsoup4

CMD chmod +x run.sh && \
    bash run.sh