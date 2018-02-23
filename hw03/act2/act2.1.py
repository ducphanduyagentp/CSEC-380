from our_spiderman import *
from my_socks import *

HOST = 'www.rit.edu'
PORT = 443

def main():

    # spider = Spiderman('https://www.rit.edu', HOST, PORT)

    # emails = spider.crawl_emails('https://www.rit.edu/gccis/computingsecurity/people')
    # for e in emails:
    #     print e

    # links = spider.crawl_urls('https://www.rit.edu/')
    # for l in links:
    #     print l


    # s1 = HTTPSocket('www.northwesternmutual.com', PORT)
    # s1.create(secure=True)

    # r = s1.get('https://www.northwesternmutual.com/')
    # print r['request']
    # print r['data']
    # print r['header']

    # s1 = HTTPSocket('www.macys.com', PORT)
    # s1.create(secure=True)
    # r = s1.get('https://www.macys.com/')
    # print r['request']
    # print r['data']
    # print r['header']['status']

    spider1 = Spiderman('https://www.northwesternmutual.com', PORT)

    links = spider1.crawl_urls('https://www.northwesternmutual.com')
    for l in links:
        print l


if __name__ == '__main__':
    main()
