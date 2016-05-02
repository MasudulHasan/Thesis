import time
import urllib
from urllib import urlopen
import re
import cookielib, urllib
from cookielib import CookieJar
import datetime

cj = CookieJar()
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://www.huffingtonpost.com/feeds/index.xml'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'',sourceCode)
            links = re.findall(r'(.*?)',sourceCode)
            for title in titles:
                print title
            for link in links:
                print link
        except Exception as e:
            print str(e)

    except Exception as e:
        print str(e)
        pass

main()