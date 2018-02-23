from our_spiderman import *
from my_socks import *
import sys
import urlparse


def main():
    parsed = urlparse.urlparse(sys.argv[1])
    HOST = urlparse.urlunparse((parsed[0], parsed[1].strip('\r\n'), '', '', '', ''))
    PORT = 80 if HOST.startswith('http://') else 443
    spider = Spiderman(HOST, PORT)
    spider.crawl_like_nobody_is_watching(depth=4)


if __name__ == '__main__':
    main()
