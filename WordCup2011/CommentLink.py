import string
import urllib
import urllib.request
import re
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
import openpyxl
from bs4 import BeautifulSoup
import re
import datetime

from xdg.Locale import regex

TotalCount=1
def content(theurl, label, fileIn=None):
    # print(theurl)
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('div', class_="each-comm")
        # print(div)
        wb = openpyxl.load_workbook('comment.xlsx')
        sheet = wb.active
        global TotalCount
        for Div in div:
            comments = Div.findAll('p',class_="fontsize")
            span=Div.find('span')
            # print(len(span))
            # print(span)
            # print(comments)
            # print('\n\n')
            date=""
            for element in span:
                element=str(element)
                element=element.strip()
                # print("elele "+str(element))
                if(element.startswith("on")):
                    date=element
                # print('\n\n')
            # print("Date "+date)
            for line in comments:
                line=str(line)
                line = re.sub('<p.*>', ' ', str(line))
                line = re.sub('</p>', ' ', str(line))
                line=line.strip()
                # print(line)
                sheet["A" + str(TotalCount)] = line
                sheet["C" + str(TotalCount)] =date
                sheet["B" + str(TotalCount)] = label
                TotalCount+=1
        wb.save('comment.xlsx')


    except Exception as e:
        print("No comment")
        str(e)

def main():
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/753287.html"
    # content(theurl)
    line_number = 1
    s1 = ""
    I=0
    with open('MatchDetail.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s = a_line.rstrip()
            if (s != " "):
                # s = a_line.rstrip()
                # print("HII"+s)
                try:
                    if (s.startswith("Label")):
                        # target.write(s+'\n')
                        # print('here')
                        s1 = s
                        # print("Here " + s)
                        print(s)
                    else:
                        content(s, s1)
                        line_number += 1
                except Exception as e:
                    print("Here" + s)
                I=I+1;
                # if(I==5):
                #     break
    print("Total Count : ",TotalCount)

main()
