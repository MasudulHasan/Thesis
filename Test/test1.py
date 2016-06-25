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
        div = soup.find_all('div', class_="teams")
        # print(div.find_all('a'))
        for line in div:
            links = line.findAll('a')
            for a in links:
                # print
                s = ''.join(a.findAll(text=True))
                print(s)
                target.write(s)
                target.write('\n')
                var = 'http://www.espncricinfo.com' + a['href']
                target.write(var)
                target.write('\n')
                print(var)

            # s = str(links)
            # s=s+'\n'
            # print(s)
            # print('\n')
            # target.write(s)

    except Exception as e:
        print
        str(e)

def main():
    theurl = "http://www.espncricinfo.com/ci/engine/series/index.html?season=2014;view=season"
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
