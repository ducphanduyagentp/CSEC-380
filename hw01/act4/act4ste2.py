import sys
import requests

def getRequest(url, proxies):
	return requests.get(url, proxies=proxies)

def proxy(ip, port):
	return "http:{}:{}".format(ip, port)

def main():
	

if __name__ == '__main__':
	main()
