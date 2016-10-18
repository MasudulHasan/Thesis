import urllib
import urllib.request
import sys, os

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime

comments=[]

TotalCount=0
dateCount=0
def content(theurl,label):
    print(label)
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
            # print(str(i))
            global TotalCount
            serial = TotalCount+1
            wb = openpyxl.load_workbook('worldcupcomments.xlsx')
            sheet = wb.active

            prevcount = TotalCount
            for node in line.findAll('p'):
                if(i%2!=0):
                    s=str(' '.join(node.findAll(text=True)))
                    # print(i+''.join(node.findAll(text=True)))
                    # s=str(k)+(s);
                    # print('test ' + s)

                    global comments

                    if(s not in comments):
                        i = len(comments)-1
                        flag=False
                        for j in range(20):
                            if(i<0):
                                break
                            if(s in comments[i]):
                                flag=True
                                break
                            i -= 1

                        if flag:
                            continue

                        comments += [s]

                        # sheet["A"+str(TotalCount)] = TotalCount
                        # print("Test: " + s)
                        TotalCount+=1
                        sheet["A"+str(TotalCount)] = str(s)
                        # print(TotalCount)
                    # target.write(s)
                    k=k+1
                i=i+1
            print(TotalCount)

            prevcount = TotalCount - prevcount
            # print(str(prev))

            for node in line.findAll('span', 'date'):
                s1=str(' '.join(node.findAll(text=True)))
                # s = str(i)+' ' + ' '.join(node.findAll(text=True))

                sheet["B"+str(serial)] = s1
                sheet["C"+str(serial)] = label
                global dateCount
                dateCount+=1
                if(serial==TotalCount):
                    break
                serial += 1

            print("Date: " + str(dateCount))

            wb.save('worldcupcomments.xlsx')

    except Exception as e:
        print("comment exception: " + str(e))
        print("latest comment: " + comments[TotalCount-1])
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        # str(e)
    # wb.save('comment_test.xlsx')

import re
def main():
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/753287.html"
    # content(theurl)
    line_number = 1
    s1 = ""
    with open('ArticleLinks.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s = a_line.strip()
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