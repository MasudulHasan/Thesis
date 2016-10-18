import string
import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
import openpyxl
from bs4 import BeautifulSoup
import re
import datetime

TotalCount=1
def content(theurl,label):
    # print(theurl)
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('ul', class_="container-tab all")
        # print(div)
        #links = div.find_all('div', class_="user-comments")
        # print(links)
        wb = openpyxl.load_workbook('comment_test.xlsx')
        sheet = wb.active
        for line in div:
            # links = line.find_all('p')
            # print(links.contents[0].strip())
            i=1
            k=1
            global TotalCount
            for CommentList in line.findAll('li'):
                # print(List)
                # s=""
                comment=CommentList.findAll('p')
                # print(len(comment))
                lst=list()
                try:
                    for s in comment:
                        # new_str=string.replace(s, '<p>',"")
                        # s = string.replace(s, '</p>',"")
                        # print(s.findAll(text=True))
                        # print(s)
                        lst.append(s)
                except Exception as e:
                    print("HRE "+e)
                s=""
                I=0
                elementSofar=set()
                for element in lst:
                    element=str(element).replace('<p>', ' ')
                    element = str(element).replace('</p>', ' ')
                    element = str(element).strip()
                    # print("Element "+element)
                    if(element not in elementSofar):
                        if(I>0):
                            s+=str(element)
                            elementSofar.add(element)
                    I+=1
                # print(str(TotalCount)+" "+s)
                sheet["A" + str(TotalCount)] = s


                date = CommentList.find('span', class_='date')
                s1 = str(' '.join(date.findAll(text=True)))
                # s = str(i) + ' ' + ' '.join(date.findAll(text=True))
                # print(i+''.join(node.findAll(text=True)))
                # print(s1)
                sheet["B" + str(TotalCount)] = label
                sheet["C" + str(TotalCount)] = s1
                TotalCount += 1

        wb.save('comment_test.xlsx')
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
                #      break
    print("Total Count : ",TotalCount)

main()
