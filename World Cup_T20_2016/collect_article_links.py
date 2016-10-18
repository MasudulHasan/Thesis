import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime

from numpy.distutils.fcompiler import none

dupcheck = []
dupset = set()
target = open("ArticleLinks.txt", 'w')

def content(theurl,label):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    # print("HERE "+theurl+'\n')
    target.write("Label: "+label+'\n')
    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('p', "SpecialsHead")
        # print(div.find_all('a'))

        for line in div:
            links = line.findAll('a')
            for a in links:
                # print
                # if 'story'in a['href']:
                #     print('found a url with Story in the link')
                var = 'http://www.espncricinfo.com' + a['href']
                # print(var)
                dupset.add(var)
                global dupcheck
                if var not in dupcheck:
                    # print(var)
                    dupcheck += [var]
                    target.write(var)
                    target.write('\n')
        print(str(len(dupcheck)))
        print(str(len(dupset)))

    except Exception as e:
        print
        str(e)
    target.write('\n\n\n')

def main():
    # theurl = "http://www.espncricinfo.com/ci/engine/series/667885.html"
    # content(theurl)
    line_number = 1
    i=0;
    s1 = ""
    temp=0
    with open('MatchLinks.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s=a_line.strip()
            # print("HII"+s)
            if (i % 2 == 0):
                # target.write(s+'\n')
                # print('here')
                # if 'ODI' in s:
                    # print(s)
                 s1=s
                # print(s1)
            else:
                content(s,s1)
                line_number += 1
                temp=0
            i=i+1

main()
