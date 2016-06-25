import urllib2
# import urllib.request
# from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime


def content():
    #theurl = a
    # thepage = urllib.request.urlopen("http://www.espncricinfo.com/ci/engine/series/index.html?season=2014;view=season")
    # soup = BeautifulSoup(thepage, "html.parser")
    target = open("foo1.txt", 'a')
    try:
        # line1 = soup.find('div', {"class": "teams"}).findAll('a')
        # s = str(line1)
        # print(s)
        # target.write(s)
        resp = urllib2.urlopen("http://www.espncricinfo.com/ci/engine/series/index.html?season=2014;view=season")
        soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

        for link in soup.find_all('a', href=True):
            if link['href']== '#':
                print 'found a url with national-park in the link'
            else:
                s = str(link)
                # print(s)
                target.write(s)
                print link

    except Exception as e:
        print
        str(e)

def main():
    #theurl = "http://www.espncricinfo.com/icc-world-twenty20-2016/content/story/990899.html"
    content()

main()
