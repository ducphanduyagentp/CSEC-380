from mySocks import *

HOSTNAME = 'csec380-core.csec.rit.edu'
PORT = 82


def main():
    s = httpSocket(HOSTNAME, PORT)
    token = s.post('http://{}:{}/getSecure'.format(HOSTNAME, PORT))
    token = token['data']
    token = token.strip('"').split(': ')[1]

    r = s.post('http://{}:{}/getFlag3Challenge'.format(HOSTNAME, PORT), query={'token': token})
    r = r['data'].strip('"').split(': ')[1]
    solution = eval(r)
    r = s.post('http://{}:{}/getFlag3Challenge'.format(HOSTNAME, PORT), query={'token': token, 'solution': solution})
    print r['data'].strip('"')


if __name__ == '__main__':
    main()
