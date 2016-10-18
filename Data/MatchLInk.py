import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime

from numpy.distutils.fcompiler import none


def content(theurl,label):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    target = open("ODIMatchDetail.txt", 'a')
    # print("HERE "+label+'\n')
    target.write("Label: "+label+'\n')
    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('ul', class_="reports-list")
        # print(div.find_all('a'))
        i = 1
        for line in div:
            links = line.findAll('a')
            for a in links:
                # print
                if 'story/index'in a['href']:
                    # print('found a url with Story in the link')
                    var = 'http://www.espncricinfo.com' + a['href']
                    # var=str(i)+" "+var
                    target.write(var)
                    target.write('\n')
                    # print(var)
                    i=i+1
            # s = str(links)
            # s=s+'\n'
            # print(s)
            # print('\n')
            # target.write(s)

    except Exception as e:
        print
        str(e)
    target.write('\n\n\n')

def main():
    # theurl = "http://www.espncricinfo.com/ci/engine/series/667885.html"
    # content(theurl)
    line_number = 1
    i=0;
    target = open("MatchDetail.txt", 'a')
    s1 = ""
    temp=0
    with open('MatchLink.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s=a_line.rstrip()
            # print("HII"+s)
            if (i % 2 == 0):
                # target.write(s+'\n')
                # print('here')
                if 'ODI' in s:
                    # print(s)
                    s1=s
                # print(s1)
            else:
                content(s,s1)
                line_number += 1
                temp=0
            i=i+1

main()
