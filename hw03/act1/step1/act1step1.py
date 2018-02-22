from my_socks import *
from bs4 import BeautifulSoup

HOST = 'www.rit.edu'
PORT = 80


def courseEntry(tag):
    data = tag.find_all('td')
    return len(data) == 3 and '-' in data[0].string


def main():
    s = HTTPSocket(HOST, PORT)
    s.create()

    html = s.get("https://www.rit.edu/programs/computing-security-bs")['data']
    html = html.decode('utf-8')
    s.close()

    soup = BeautifulSoup(html, 'html.parser')
    courses = soup.find_all(courseEntry)
    
    result = []
    for course in courses:
        course = course.find_all('td')
        result.append('{}: {}'.format(course[0].string.replace(u'\xa0', u'').strip(' '), course[1].string.replace(u'\xa0', u'').strip(' ')))
    
    result.sort()
    
    for r in result:
        print r


if __name__ == '__main__':
    main()
