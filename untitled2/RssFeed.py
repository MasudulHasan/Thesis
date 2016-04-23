import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://www.espncricinfo.com/rss/content/story/feeds/34102.rss'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'<guid>(.*?)</guid>',sourceCode)
            links = re.findall(r'<link.*?href=\"(.*?)\"',sourceCode)
            i=1
            target = open("C:\Users\Batman\PycharmProjects\RssFeed\Rohit.txt", 'a')
            for title in titles:
                print i
                i += 1
                s = str(title+'\n')
                target.write(s)
                print title

        except Exception, e:
            print str(e)





    except Exception,e:
        print str(e)
        pass

main()