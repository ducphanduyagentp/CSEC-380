import socket
from urlparse import urlparse

HOSTNAME = 'csec380-core.csec.rit.edu'
PORT = 82


class httpSocket:

    httpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    useragent = 'supersecretagent'

    def __init__(self, hostname, port):
        ip = socket.gethostbyname(hostname)
        try:
            self.httpSock.connect((ip, port))
        except:
            print 'Error creating socket'
            exit(1)

    def recvHTTPHeader(self):
        header = ''
        while True:
            b = self.httpSock.recv(1)
            header += b
            if header.endswith('\n' * 2) or header.endswith('\r\n' * 2):
                break
        realHeader = {}
        header = header.split('\r\n')
        header = [hdr.strip().split(': ') for hdr in header if hdr != '']
        realHeader['status'] = header[0][0].split(' ')[1]
        for hdr in header[1:]:
            realHeader[hdr[0]] = hdr[1]
        return realHeader

    def get(self, url, params={}, query={}, useragent=useragent):
        parsed = urlparse(url)
        payload = "GET {} HTTP/1.1\n".format(parsed.path)
        payload += "Host: {}\n".format(parsed.netloc)
        payload += "User-Agent: {}\n".format(useragent)
        payload += "Accept: */*\n"
        payload += "\n"
        self.httpSock.send(payload)
        header = self.recvHTTPHeader()
        data = self.httpSock.recv(int(header['Content-Length']))
        return {'header': header, 'data': data}

    def post(self, url, params={}, query={}, useragent=useragent):
        parsed = urlparse(url)
        payload = "POST {} HTTP/1.1\n".format(parsed.path)
        payload += "Host: {}\n".format(parsed.netloc)
        payload += "User-Agent: {}\n".format(useragent)
        payload += "Accept: */*\n"
        payload += "\n"


def main():
    s = httpSocket(HOSTNAME, PORT)
    print s.get('http://csec380-core.csec.rit.edu:82/')


if __name__ == '__main__':
    main()
