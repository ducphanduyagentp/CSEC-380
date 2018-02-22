import socket
from urlparse import urlparse



class HTTPSocket:
    CRLF = '\r\n'
    useragent = 'supersecretagent'
    HTTPSock = None

    def __init__(self, hostname, port):
        self.HOST = hostname
        self.PORT = port
        self.IP = socket.gethostbyname(hostname)

    def create(self):
        if self.HTTPSock == None:
            self.HTTPSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.HTTPSock.connect((self.IP, self.PORT))
        except:
            print 'Error creating socket:'
            raise
            exit(1)
        

    def close(self):
        self.HTTPSock.shutdown(socket.SHUT_RDWR)
        self.HTTPSock.close()

    def recvuntil(self, pattern):
        data = ''
        while pattern not in data:
            data += self.HTTPSock.recv(1)
        return data

    def recvdata(self, header):
        if 'Transfer-Encoding' in header and header['Transfer-Encoding'] == 'chunked':
            data = ''
            while True:
                length = self.recvuntil(self.CRLF)
                length = int(length, 16)
                if length == 0:
                    break
                data += self.HTTPSock.recv(length)
                self.recvuntil(self.CRLF)
        else:
            data = self.HTTPSock.recv(int(header['Content-Length']))
        return data

    def recvHTTPHeader(self):
        header = ''
        while True:
            b = self.HTTPSock.recv(1)
            header += b
            if header.endswith(self.CRLF * 2):
                break
        realHeader = {}
        header = header.split(self.CRLF)
        header = [hdr.strip().split(': ') for hdr in header if hdr != '']
        realHeader['status'] = header[0][0].split(' ')[1]
        for hdr in header[1:]:
            realHeader[hdr[0]] = hdr[1]
        return realHeader

    def get(self, url, otherHeaders={}, params={}, query={}, useragent=useragent):
        data = '?' + '&'.join(['{}={}'.format(k, v) for k, v in zip(query.keys(), query.values())])
        parsed = urlparse(url)
        payload = "GET {} HTTP/1.1".format(parsed.path + (data if len(data) > 1 else '')) + self.CRLF
        payload += "Host: {}".format(self.HOST + ('' if self.PORT == 80 else ':{}'.format(self.PORT))) + self.CRLF
        payload += "User-Agent: {}".format(useragent) + self.CRLF
        payload += "Accept: */*" + self.CRLF
        payload += self.CRLF.join(['{}: {}'.format(k, v) for k, v in zip(otherHeaders.keys(), otherHeaders.values())])
        payload += self.CRLF * 2

        t = self.HTTPSock.sendall(payload)
        assert t == None
        header = self.recvHTTPHeader()
        data = self.recvdata(header)
        return {'request': payload, 'header': header, 'data': data}

    def post(self, url, params={}, query={}, useragent=useragent):
        data = '&'.join(['{}={}'.format(k, v) for k, v in zip(query.keys(), query.values())])
        parsed = urlparse(url)
        payload = "POST {} HTTP/1.1".format(parsed.path) + self.CRLF
        payload += "Host: {}".format(parsed.netloc) + self.CRLF
        payload += "User-Agent: {}".format(useragent) + self.CRLF
        payload += "Accept: */*" + self.CRLF
        payload += "Content-Type: application/x-www-form-urlencoded" + self.CRLF
        payload += "Content-Length: {}".format(len(data)) + self.CRLF
        payload += self.CRLF
        payload += data + self.CRLF
        self.HTTPSock.send(payload)
        header = self.recvHTTPHeader()
        data = self.recvdata(header)
        return {'request': payload, 'header': header, 'data': data}

    def postRaw(self, payload):
        self.HTTPSock.send(payload)
        header = ""
        while True:
            header += self.HTTPSock.recv(1)
            if header.endswith(self.CRLF * 2):
                break

        response = ''
        while True:
            response += self.HTTPSock.recv(1)
            if response.endswith(self.CRLF * 2):
                break

        return {'header': header, 'response': response}
