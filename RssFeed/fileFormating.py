import urllib
import urllib.request
from http.cookiejar import CookieJar

from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime

def main():
    #theurl = "http://www.espncricinfo.com/icc-world-twenty20-2016/content/story/990899.html"
    #content(theurl)
    line_number = 1
    target = open("onlycomment.txt", 'a')
    mainString=str(" ")
    with open('player.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            #print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s=a_line.rstrip()
            #s=str(a_line)
            #print(s)
            s1="</p>, <p>"
            if((s==s1)or(s=='</p>')or(s=='<p>')):
                #print("nothing")
                line_number +=1
            else:
                #s = s.encode('cp850', errors='replace')
                #s = str(s)
                #target.write(s)
                #target.write(s)
                #target.write("\n")
                mainString=mainString+s+"\n"

            #content(s)
            line_number += 1
    SS=str(mainString.encode("utf-8"))
    target.write(SS)

main()
