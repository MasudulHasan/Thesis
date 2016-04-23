import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import urllib
import urllib.request

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
    target = open("top1.txt", 'a')
    line1 = soup.find('div', {"class": "user-comments"}).findAll('p')
    #s = str(line1)
    #target.write(s)
    #print(s)
    #target.write(s)
    for letter in line1:  # First Example
        #print(letter)
        s = str(letter)
        s= s.encode('cp850', errors='replace')
        s=str(s)
        target.write(s)


def main():
    theurl = "http://www.espncricinfo.com/indian-premier-league-2016/content/story/1001357.html"
    content(theurl)

main()
#print(soup.find('div',{"class":"user-comments"}).findAll('p'))