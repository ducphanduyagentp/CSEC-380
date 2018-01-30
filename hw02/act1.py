from mySocks import *

HOSTNAME = 'csec380-core.csec.rit.edu'
PORT = 82


def main():
    s = httpSocket(HOSTNAME, PORT)
    print s.post('http://csec380-core.csec.rit.edu:82/')['data']


if __name__ == '__main__':
    main()
