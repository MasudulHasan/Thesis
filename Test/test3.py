import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime


def content(theurl,label):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    target = open("ODIArticleLink.txt", 'a')
    target.write("Label: " + label + '\n')
    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('p', class_="SpecialsHead")
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
                # print(var)
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
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/index.html?object=667899"
    # content(theurl)
    line_number = 1
    s1=""
    with open('ODIMatchDetail.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s = a_line.rstrip()
            if(s!=" "):
                # s = a_line.rstrip()
                # print("HII"+s)
                try:
                    if (s.startswith("Label")):
                        # target.write(s+'\n')
                        # print('here')
                        s1 = s
                        # print("Here "+s)
                        # print(s1)
                    else:
                        content(s, s1)
                        line_number += 1
                except Exception as e:
                    print("Here"+s)
main()
