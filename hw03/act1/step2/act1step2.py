import os

from my_socks import *
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

HOST = 'www.rit.edu'
PORT = 80
DIRECTORY = './a1.2-images'

def get_image(url):
    s = HTTPSocket(HOST, PORT)
    s.create()

    url = 'http://www.rit.edu{}'.format(url)
    r = s.get(url, otherHeaders={'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate'})
    s.close()

    assert int(r['header']['status']) == 200
    data = r['data']

    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

    filename = DIRECTORY + '/{}'.format(url.split('/')[-1])
    f = open(filename, 'w')
    f.write(data)
    f.close()


def main():
    s = HTTPSocket(HOST, PORT)
    s.create()

    html = s.get("http://www.rit.edu/gccis/computingsecurity/people", otherHeaders={'Connection': 'keep-alive'})
    s.close()

    html = html['data']
    html = html.decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('div', {'class': 'staff'})
    images = [x.find('img')['src'] for x in images]
    
    pool = ThreadPool(500)
    pool.map(get_image, images)

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
