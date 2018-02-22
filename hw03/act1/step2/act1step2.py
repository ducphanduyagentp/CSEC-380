from my_socks import *
from bs4 import BeautifulSoup

HOST = 'www.rit.edu'
PORT = 80

def main():
    s = HTTPSocket(HOST, PORT)
    html = s.get("http://www.rit.edu/gccis/computingsecurity/people")['data']
    html = html.decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('div', {'class': 'staff'})
    images = [x.find('img')['src'] for x in images]
    for e in images:
        print e

if __name__ == '__main__':
    main()
