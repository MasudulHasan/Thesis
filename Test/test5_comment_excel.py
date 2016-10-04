import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime

TotalCount=0
def content(theurl,label):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    import openpyxl

    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('ul', "all")
        # print('div' + div)
        #links = div.find_all('div', class_="user-comments")
        # print(links)
        for line in div:
            # links = line.find_all('p')
            # print(links.contents[0].strip())
            i=1
            k=1
            print(str(i))
            global TotalCount
            serial = TotalCount+1
            wb = openpyxl.load_workbook('comment_test.xlsx')
            sheet = wb.active

            for node in line.findAll('p'):
                if(i%2!=0):
                    TotalCount += 1
                    print(TotalCount)
                    s=str(' '.join(node.findAll(text=True)))
                    # print(i+''.join(node.findAll(text=True)))
                    # s=str(k)+(s);
                    # print('test ' + s)
                    sheet["A"+str(TotalCount)] = TotalCount
                    sheet["B"+str(TotalCount)] = s
                    # target.write(s)
                    k=k+1
                i=i+1

            i=1

            for node in line.findAll('span', 'date'):
                s1=str(' '.join(node.findAll(text=True)))
                # s = str(i)+' ' + ' '.join(node.findAll(text=True))
                sheet["C"+str(serial)] = s1
                sheet["D"+str(serial)] = label
                serial += 1

            wb.save('comment_test.xlsx')

    except Exception as e:
        print("comment exception: " + str(e))
        # str(e)
    # wb.save('comment_test.xlsx')

import re
def main():
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/753287.html"
    # content(theurl)
    line_number = 1
    s1 = ""
    with open('ODIArticleLink.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s = a_line.rstrip()
            # if (s != " "):
            try:
                if (s.startswith("Label")):
                    s1 = re.sub('Label: ', '', s)       #don't need the word "label"
                else:
                    content(s, s1)
                    line_number += 1
                    # print(str(line_number))
            except Exception as e:
                print("Here " + str(e))
    print("Total Count : ",TotalCount)

main()

def main2():
    content("http://www.espncricinfo.com/ireland/content/story/742397.html", "Sri Lanka in Ireland ODI Series")

# main2()