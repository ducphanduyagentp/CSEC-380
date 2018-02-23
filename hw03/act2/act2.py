from our_spiderman import *
from my_socks import *

PORT = 443

def main():

    spider = Spiderman('https://www.rit.edu', PORT)

    links = spider.crawl_urls('https://www.rit.edu/')
    for l in links:
        print l


if __name__ == '__main__':
    main()
