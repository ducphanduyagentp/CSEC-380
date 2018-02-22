import socket
from urlparse import urlparse



class HTTPSocket:
    CRLF = '\r\n'
    HTTPSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    useragent = 'supersecretagent'

    def __init__(self, hostname, port):
        ip = socket.gethostbyname(hostname)
        try:
            self.HTTPSock.connect((ip, port))
        except:
            print 'Error creating socket:'
            exit(1)

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
            if header.endswith('\n' * 2) or header.endswith(self.CRLF * 2):
                break     
        realHeader = {}
        header = header.split(self.CRLF)
        header = [hdr.strip().split(': ') for hdr in header if hdr != '']
        realHeader['status'] = header[0][0].split(' ')[1]
        for hdr in header[1:]:
            realHeader[hdr[0]] = hdr[1]
        return realHeader

    def get(self, url, params={}, query={}, useragent=useragent):
        data = '?' + '&'.join(['{}={}'.format(k, v) for k, v in zip(query.keys(), query.values())])
        parsed = urlparse(url)
        payload = "GET {} HTTP/1.1\r\n".format(parsed.path + data)
        payload += "Host: {}\r\n".format(parsed.netloc)
        payload += "User-Agent: {}\r\n".format(useragent)
        payload += "Accept: */*\r\n"
        payload += "Connection: keep-alive\r\n"
        payload += "\r\n"
        self.HTTPSock.send(payload)
        header = self.recvHTTPHeader()
        data = self.recvdata(header)
        return {'request': payload, 'header': header, 'data': data}

    def post(self, url, params={}, query={}, useragent=useragent):
        data = '&'.join(['{}={}'.format(k, v) for k, v in zip(query.keys(), query.values())])
        parsed = urlparse(url)
        payload = "POST {} HTTP/1.1\r\n".format(parsed.path)
        payload += "Host: {}\r\n".format(parsed.netloc)
        payload += "User-Agent: {}\r\n".format(useragent)
        payload += "Accept: */*\r\n"
        payload += "Content-Type: application/x-www-form-urlencoded\r\n"
        payload += "Content-Length: {}\r\n".format(len(data))
        payload += "\r\n"
        payload += data + '\n'
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
