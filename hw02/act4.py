from mySocks import *
import zlib
import urllib

HOSTNAME = 'csec380-core.csec.rit.edu'
PORT = 82


def fakeIEHeader(path, data):
    header = "POST {} HTTP/1.1\n".format(path)
    header += "Accept: text/html, application/xhtml+xml, image/jxr, */*\n"
    header += "Accept-Language: en-US\n"
    header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko\n"
    header += "Accept-Encoding: gzip, deflate\n"
    header += "Host: csec380-core.csec.rit.edu:82\n"
    header += "Connection: keep-alive\n"
    header += "Content-Length: {}\n".format(len(data))
    header += "Content-Type: application/x-www-form-urlencoded\n"
    header += "\n"
    return header


def main():

    s = httpSocket(HOSTNAME, PORT)
    username = 'fpasswd'
    token = s.post('http://{}:{}/getSecure'.format(HOSTNAME, PORT))
    token = token['data']
    token = token.strip('"').split(': ')[1]

    data = urllib.urlencode({'token': token, 'username': username})
    header = fakeIEHeader("/createAccount", data)
    payload = header + data
    password = s.postRaw(payload)
    password = password['response'].split('\r\n')[1]
    password = zlib.decompress(password, 31).split('your password is ')[1]

    data = urllib.urlencode({'token': token, 'username': username, 'password': password})
    header = fakeIEHeader("/login", data)
    payload = header + data
    login = s.postRaw(payload)
    login = login['response'].split('\r\n')[1]
    login = zlib.decompress(login, 31)
    print login.strip('"')


if __name__ == '__main__':
    main()
