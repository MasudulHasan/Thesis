import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime


def content(theurl):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    target = open("MatchLink.txt", 'a')
    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('div', class_="large-15 medium-15 small-20 columns content_data")
        # print(div.find_all('a'))
        count=0
        for line in div:
            link=line.find('a')
            s1 = 'title '.join(link.findAll(text=True))
            # print(s)
            # if "Bangladesh" in s:
            #     print("BANGLAdesh  "+s)
            links = line.findAll('a')
            for a in links:
                # print
                s = ''.join(a.findAll(text=True))
                print(s)
                if "Articles" in s:
                    target.write(s1)
                    # target.write('\n')
                    var = 'http://www.espncricinfo.com' + a['href']
                    target.write(var)
                    # target.write('\n')
                    print(var)
            count=count+1
        print(count)

            # s = str(links)
            # s=s+'\n'
            # print(s)
            # print('\n')
            # target.write(s)

    except Exception as e:
        print
        str(e)

def main():
    theurl = "http://www.espncricinfo.com/icc-cricket-world-cup-2015/engine/series/509587.html"
    content(theurl)
    # line_number = 1
    # with open('boo.txt', encoding='utf-8') as a_file:
    #     for a_line in a_file:
            #print('{:>4} {}'.format(line_number, a_line.rstrip()))
            # s=a_line.rstrip()
            # print(s)
            # content(s)
            # line_number += 1

main()
