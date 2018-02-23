import os
import re

from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from urlparse import urlparse, urlunparse
from my_socks import *


class Spiderman:

    def __init__(self, url, port):
        parsed = urlparse(url)
        self.SCHEME = parsed.scheme
        self.HOST = parsed.netloc
        self.PORT = port
        self.URL = url

    def is_in_scope(self, url):
        parsed = urlparse(url)
        return self.HOST == parsed.netloc or \
        (parsed.netloc == '' and parsed.path != '' and \
        (':' not in parsed.path or \
        '@' not in parsed.path or \
        '#' not in parsed.path))

    def calculate_depth(self, url):
        parsed = urlparse(url)
        path = parsed.path
        while '//' in path:
            path = path.replace('//', '/')
        path = path.rstrip('/')
        return path.count('/')

    def normalizeURLs(self, urls):
        for i in xrange(len(urls)):
            u = urls[i]
            urls[i] = urlunparse((self.SCHEME, self.HOST, urlparse(u).path, '', '', ''))
        return urls

    def linkFilter(self, tag):
        return not self.emailFilter(tag) and (tag.has_attr('href') and tag['href'] != '#')

    def emailFilter(self, tag):
        return tag.has_attr('href') and 'mailto:' in tag['href'] and '@' in tag['href']

    def getPage(self, url):
        s = HTTPSocket(self.HOST, self.PORT)
        if self.PORT == 443:
            s.create(secure=True)
        else:
            s.create()

        try:
            html = s.get(url)
            html = html['data']
            html = html.decode('utf-8')
        except:
            print 'Error getting response'
            raise
            exit(1)
        return html

    def crawl_emails(self, url):
        html = self.getPage(url)
        soup = BeautifulSoup(html, 'html.parser')
        emails = soup.find_all(self.emailFilter)
        emails = [e.text for e in emails]
        return emails

    def crawl_urls(self, url):
        html = self.getPage(url)
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all(self.linkFilter)
        links = [link['href'] for link in links if self.is_in_scope(link['href'])]
        return list(set(self.normalizeURLs(links)))

    def crawl_all_emails(self, depth=1):
        pass

    def crawl_all_urls(self, depth=1, file=None):
        result = []
        links = crawl_urls(self.URL)



