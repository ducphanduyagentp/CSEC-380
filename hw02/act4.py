from mySocks import *

HOSTNAME = 'csec380-core.csec.rit.edu'
PORT = 82


def main():
    useragent = "IE"

    s = httpSocket(HOSTNAME, PORT)

    token = s.post('http://{}:{}/getSecure'.format(HOSTNAME, PORT), useragent=useragent)
    token = token['data']
    token = token.strip('"').split(': ')[1]

    r = s.post('http://{}:{}/createAccount'.format(HOSTNAME, PORT), query={'token': token, 'username': 'ggwp'}, useragent=useragent)
    print r['request']
    print r['data']


if __name__ == '__main__':
    main()
