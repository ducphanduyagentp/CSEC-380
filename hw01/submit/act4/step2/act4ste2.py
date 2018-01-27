import sys
import requests
import netaddr
from multiprocessing.dummy import Pool as ThreadPool

PORTS = [80, 8080, 8123, 3128, 8000]


def getRequest(url, proxies):
    return requests.get(url, proxies={'http': proxies}, timeout=5.0)


def proxy(ip, port):
    return "http://{}:{}".format(ip, port)


def checkProxy(ip):
    global PORTS
    ip = str(netaddr.IPAddress(ip))
    for port in PORTS:
        try:
            r1 = getRequest('http://www.0xf.tech/', proxy(ip, port))
            if r1.status_code == 200 and \
            '<title>ComChat: Making close distance closer</title>' in r1.text:
                print '{}:{}'.format(ip, port)
                return
        except:
             pass


def main():
    if len(sys.argv) != 3:
        print 'Usage: act4ste2.py <start-ip> <end-ip>'
        exit(1)
    startIP = netaddr.IPAddress(sys.argv[1])
    endIP = netaddr.IPAddress(sys.argv[2])

    pool = ThreadPool(500)
    r = pool.map(checkProxy, range(int(startIP), int(endIP) + 1))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
