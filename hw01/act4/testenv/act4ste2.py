import sys
import requests
import netaddr

PORTS = [80, 8080]

def getRequest(url, proxies):
    return requests.get(url, proxies= {'http': proxies})

def proxy(ip, port):
    return "http://{}:{}".format(ip, port)

def main():
    global PORTS
    if len(sys.argv) != 3:
        print 'Usage: act4ste2.py <start-ip> <end-ip>'
        exit(1)
    startIP = netaddr.IPAddress(sys.argv[1])
    endIP = netaddr.IPAddress(sys.argv[2])
    for ip in xrange(int(startIP), int(endIP) + 1):
        ipStr = str(netaddr.IPAddress(ip))
        for port in PORTS:
            try:
                r = getRequest('http://csec.rit.edu', proxy(ipStr, port))
                if r.status_code == 200:
                    print '{}:{}'.format(ipStr, port)
                    break
            except:
                pass

if __name__ == '__main__':
    main()
