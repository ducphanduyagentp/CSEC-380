import socket
from urlparse import urlparse

HOSTNAME = 'csec380-core.csec.rit.edu'
PORT = 82


class httpSocket:

    httpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, hostname, port):
        ip = socket.gethostbyname(hostname)
        try:
            self.httpSock.connect((ip, port))
        except:
            print 'Error creating socket'
            exit(1)

    def recvHTTPHeader(self):
        pass

    def get(self, url, useragent='supersecretagent'):
        parsed = urlparse(url)
        payload = "GET {} HTTP/1.1\n".format(parsed.path)
        payload += "Host: {}\n".format(parsed.netloc)
        payload += "User-Agent: {}\n".format(useragent)
        payload += "Accept: */*\n"
        payload += "\n"
        self.httpSock.send(payload)
        header = self.recvHTTPHeader()
        data = self.httpSock.recv(int(header.contentLength))
        return {'header': header, 'data': data}


def main():
    s = httpSocket(HOSTNAME, PORT)
    s.get('http://csec380-core.csec.rit.edu:82/')


if __name__ == '__main__':
    main()
