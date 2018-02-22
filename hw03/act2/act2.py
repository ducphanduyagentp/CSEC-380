import os

from my_socks import *
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

HOST = 'www.rit.edu'
PORT = 443

def main():
    s = HTTPSocket(HOST, PORT)
    s.create(secure=True)

    r = s.get('https://www.rit.edu/')
    print r['request']
    print r['data']


if __name__ == '__main__':
    main()
