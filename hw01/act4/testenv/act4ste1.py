import requests

def main():
	r = requests.get('http://csec.rit.edu')
	if r.status_code == 200:
		print r.text

if __name__ == '__main__':
	main()
