from our_spiderman import *
from my_socks import *
import sys

HOST = 'csec380-core.csec.rit.edu'
PORT = 83
URL = 'http://csec380-core.csec.rit.edu:83/'
DEPTH = 4
s = HTTPSocket(HOST, PORT)

db = open('db.txt').readlines()
db = [d.strip(' \n') for d in db]
f = open('secrets.txt', 'w')

def isSecret(data):
    return 'YOU FOUND ME' in data


def DFS(url, depth):
    if depth > DEPTH:
        return

    print url
    global s
    s = HTTPSocket(HOST, PORT)
    s.create()
    r = s.get(url)['data']
    s.close()
    for path in db:
        v = url + path + '/'
        try:
            if isSecret(r):
                global f
                print f.write(urlparse.urlparse(v).path.rstrip('/'))
            DFS(v, depth + 1)
        except:
            pass


def main():
    DFS(URL, 0)

if __name__ == '__main__':
    main()
