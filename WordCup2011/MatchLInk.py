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

    target = open("MatchDetail.txt", 'a')
    # print("HERE "+theurl+'\n')
    target.write("Label: "+label+'\n')
    try:
        div = soup.find_all('p', class_="SpecialsHead")
        # print(div)
        # print()
        # print(div.find_all('a'))
        for line in div:
            links = line.findAll('a', class_="SpecialsHead")
            for a in links:
                # print
                # if 'story'in a['href']:
                #     print('found a url with Story in the link')
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
    target.write('\n\n')
    a = soup.find('a', href=True, class_="PaginationLink")
    if a:
        Link=theurl.split("?")
        link =Link[0]+a["href"]
        print(theurl)
        print()
        print("LINK "+link)
        print(a.text)
        s=str(a.text)
        if("Next" in s):
            content(link, label)



def main():
    # theurl = "http://www.espncricinfo.com/icc-world-twenty20-2016/content/story/index.html?object=951373"
    # content(theurl,"dfvdfv")
    line_number = 1
    i=0;
    # target = open("MatchDetail.txt", 'a')
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
