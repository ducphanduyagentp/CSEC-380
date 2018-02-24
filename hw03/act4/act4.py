from our_spiderman import *
from my_socks import *
import sys
import urllib

HOST = 'csec380-core.csec.rit.edu'
PORT = 83
URL = 'http://csec380-core.csec.rit.edu:83/'
DEPTH = 4
RUNTIME = 1000000000
s = HTTPSocket(HOST, PORT)

db = open('db.txt').readlines()
db = [d.strip(' \n') for d in db]
f = open('secrets.txt', 'w')

def isSecret(data):
    return 'YOU FOUND ME' in data


def main():
    global s, f

    q = [URL]
    for _ in xrange(RUNTIME):

        if len(q) == 0:
            break

        url = q[0].replace(' ', '+')
        if Spiderman.calculate_depth(url) > DEPTH:
            continue
        q = q[1:]

        s = HTTPSocket(HOST, PORT)
        s.create()
        r = s.get(url)
        s.close()
        print url, r['header']['status']

        if r['header']['status'] != '200':
            continue

        if isSecret(r['data']):
            f.write(urlparse.urlparse(v).path.rstrip('/'))

        if Spiderman.calculate_depth(url) == DEPTH:
            continue

        for path in db:
            v = (url + path + '/').replace(' ', '+')
            try:
                s = HTTPSocket(HOST, PORT)
                s.create()
                r = s.get(v)
                s.close()
                print v, r['header']['status']
                if r['header']['status'] != '200':
                    continue
                q.append(v)
                if isSecret(r['data']):
                    f.write(urlparse.urlparse(v).path.rstrip('/'))
            except:
                pass


if __name__ == '__main__':
    main()
