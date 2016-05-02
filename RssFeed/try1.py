import urllib
import urllib.request
from http.cookiejar import CookieJar

from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime


def content(theurl):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    """
    print(soup.title.text)
    print(soup.findAll('div'))

    fo = open("foo.txt", "wb")
    fo.write( 'Python is a great language.\nYeah its great!!');

    # Close opend file
    fo.close()
    raw_input("?")

    print "Opening the file..."
    """
    target = open("foo.txt", 'a')
    try:
        line1 = soup.find('div', {"class": "user-comments"}).findAll('p')
        s = str(line1)
        print(s)
        target.write(s)

    except Exception as e:
        print
        str(e)

def main():
    #theurl = "http://www.espncricinfo.com/icc-world-twenty20-2016/content/story/990899.html"
    #content(theurl)
    line_number = 1
    with open('boo.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            #print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s=a_line.rstrip()
            print(s)
            content(s)
            line_number += 1

main()
