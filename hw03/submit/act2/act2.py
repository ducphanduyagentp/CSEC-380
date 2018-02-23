from our_spiderman import *
from my_socks import *

PORT = 443

def main():
    spider = Spiderman('https://www.rit.edu', PORT)
    spider.crawl_like_nobody_is_watching(depth=4, email=True)
    emails = spider.get_emailDB()
    for e in emails:
        print e

if __name__ == '__main__':
    main()
