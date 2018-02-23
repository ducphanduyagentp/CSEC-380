import os
import re
import itertools

from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from urlparse import urlparse, urlunparse
from my_socks import *
from multiprocessing import Process, Lock


class Spiderman:

    def __init__(self, url, port):
        parsed = urlparse(url)
        self.SCHEME = parsed.scheme
        self.HOST = parsed.netloc
        self.PORT = port
        self.DB_URL = {}
        self.DB_EMAIL = set()
        self.visited = {}
        self.URL = url
        self.DEPTH = 1

    """
    url: The url may or may not include the hostname
    """
    def is_in_scope(self, url):
        parsed = urlparse(url)
        return self.HOST == parsed.netloc or \
        (parsed.netloc == '' and parsed.path != '' and \
        (':' not in parsed.path or \
        '@' not in parsed.path or \
        '#' not in parsed.path))

    """
    The depth of an url is calculated based on the path.
    url: The url may or may not include the hostname
    """
    def calculate_depth(self, url):
        parsed = urlparse(url)
        path = parsed.path
        while '//' in path:
            path = path.replace('//', '/')
        path = path.rstrip('/')
        return path.count('/')

    """
    url: The url may or may not include the hostname
    """
    def normalizeURLs(self, urls):
        for i in xrange(len(urls)):
            u = urls[i]
            urls[i] = urlunparse((self.SCHEME, self.HOST, urlparse(u).path, '', '', ''))
        return urls

    def linkFilter(self, tag):
        return not self.emailFilter(tag) and (tag.has_attr('href') and tag['href'] != '#')

    def emailFilter(self, tag):
        return tag.has_attr('href') and ('mailto:' in tag['href']) and ('@' in tag['href']) and (tag['href'].split('@')[1].count('.') > 0)

    """
    Get the content of the url.
    url: The url SHOULD be a full url with hostname and protocol.
    """
    def getPage(self, url):
        s = HTTPSocket(self.HOST, self.PORT)
        if self.PORT == 443:
            s.create(secure=True)
        else:
            s.create()

        try:
            html = s.get(url)
            html = html['data']
            for c in range(0x7f + 1, 0xff + 1):
                html = html.replace(chr(c), '')
            html = html.decode('utf-8')
        except:
            print 'Error getting response'
            return None
        return html

    def crawl_emails(self, url):
        html = self.getPage(url)
        if html == None:
            return []
        soup = BeautifulSoup(html, 'html.parser')
        emails = soup.find_all(self.emailFilter)
        emails = [urlparse(e['href'].split('mailto:')[1].strip(' \t\n')).path for e in emails]
        return list(set(emails))

    def crawl_urls(self, url):
        html = self.getPage(url)
        if html == None:
            return []
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all(self.linkFilter)
        links = [link['href'] for link in links if self.is_in_scope(link['href'])]
        return list(set(self.normalizeURLs(links)))

    def crawl_all_emails(self, url, depth=1):
        depth = self.DEPTH
        if self.calculate_depth(url) > depth:
            return

        links = self.crawl_urls(url)
        links = set(links)

        while len(links) > 0:

            link = links.pop()
            urlDepth = self.calculate_depth(link)

            if link in self.visited:
                continue
            elif urlDepth > depth:
                continue

            if urlDepth not in self.DB_URL:
                self.DB_URL[urlDepth] = set()
            self.DB_URL[urlDepth].add(link)
            self.visited[link] = 'True'
            emails = self.crawl_emails(link)
            for e in emails:
                print e

            self.DB_EMAIL.update(set(emails))

            subLinks = self.crawl_urls(link)
            for sublink in subLinks:
                if self.calculate_depth(sublink) > depth:
                    continue
                if sublink not in links and sublink not in self.visited:
                    links.add(sublink)

    def crawl_all_urls(self, url):
        depth = self.DEPTH
        if self.calculate_depth(url) > depth:
            return

        links = self.crawl_urls(url)
        links = set(links)

        while len(links) > 0:

            link = links.pop()
            urlDepth = self.calculate_depth(link)

            if link in self.visited:
                continue
            elif urlDepth > depth:
                continue

            if urlDepth not in self.DB_URL:
                self.DB_URL[urlDepth] = set()
            self.DB_URL[urlDepth].add(link)
            self.visited[link] = 'True'

            print link

            subLinks = self.crawl_urls(link)
            for sublink in subLinks:
                if self.calculate_depth(sublink) > depth:
                    continue
                if sublink not in links and sublink not in self.visited:
                    links.add(sublink)

    def get_emailDB(self):
        return self.DB_EMAIL

    def get_urlDB(self):
        return self.DB_URL

    def crawl_like_nobody_is_watching(self, depth=1, email=False):
        self.DEPTH = depth
        links = self.crawl_urls(self.URL)
        links = list(set(links))
        pool = ThreadPool(50)
        pool.map(self.crawl_all_urls if not email else self.crawl_all_emails, links)
        pool.close()
        pool.join()
