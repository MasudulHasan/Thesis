import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime

TotalCount=1
def content(theurl,label):
    #theurl = a
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    target = open("TEST_ODIComment-With-Hader2.txt", 'a')
    target1 = open("ODIUserName-With-Hader2.txt", 'a')
    target2 = open("ODIDate-With-Hader2.txt", 'a')
    target3 = open("ODIComments.txt", 'a')
    target4 = open("ODIUserName.txt", 'a')
    target5 = open("ODIDate.txt", 'a')
    target.write(label + '\n\n\n')
    target1.write(label + '\n\n\n')
    target2.write(label + '\n\n\n')
    # print("Label: " + label + '\n')
    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('ul', "all")
        # print(div)
        #links = div.find_all('div', class_="user-comments")
        # print(links)
        for line in div:
            # links = line.find_all('p')
            # print(links.contents[0].strip())
            i=1
            k=1
            for node in line.findAll('p'):
                if(i%2!=0):
                    global  TotalCount
                    TotalCount += 1
                    s=str(' '.join(node.findAll(text=True)))
                    # print(i+''.join(node.findAll(text=True)))
                    target3.write(s)
                    target3.write('\n')
                    s=str(k)+(s);
                    # print(s)
                    target.write(s)
                    k=k+1
                i=i+1

            i=1
            for node in line.findAll('span',class_="user_name"):
                # target4.write(' '.join(node.findAll(text=True)))
                # target4.write('\n')
                s1 = str(' '.join(node.findAll(text=True)))
                s = str(i) + ' '.join(node.findAll(text=True))
                # print(i+''.join(node.findAll(text=True)))
                # print(s)
                # s = str(i) + (s);
                # print(k,s)
                target1.write(s)
                target4.write(s1)
                # target4.write('\n')
                i = i + 1

            i = 1
            for node in line.findAll('span',class_='date'):
                # target5.write(' '.join(node.findAll(text=True)))
                # target5.write('\n')
                s1=str(' '.join(node.findAll(text=True)))
                s = str(i)+' ' + ' '.join(node.findAll(text=True))
                # print(i+''.join(node.findAll(text=True)))
                # print(s1)
                target5.write(s1)
                target5.write('\n')
                target2.write(s)
                target2.write('\n')
                i = i + 1


            # for a in links:
                # print
                # if 'story'in a['href']:
                #     print('found a url with Story in the link')
                # var = 'http://www.espncricinfo.com' + a['href']
                # target.write(var)
                # target.write('\n')
                # print(var)
            # s = str(links)
            # s=s+'\n'
            # print(s)
            # print('\n')
            # target.write(s)

    except Exception as e:
        print("No comment")
        str(e)
    target.write('\n\n\n')
    target1.write('\n\n\n')
    target2.write('\n\n\n')

def main():
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/753287.html"
    # content(theurl)
    line_number = 1
    s1 = ""
    with open('ODIArticleLink.txt', encoding='utf-8') as a_file:
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
                        # print(s1)
                    else:
                        content(s, s1)
                        line_number += 1
                except Exception as e:
                    print("Here" + s)
    print("Total Count : ",TotalCount)


def main2():
    content("http://www.espncricinfo.com/ireland/content/story/742397.html", "Label: Sri Lanka in Ireland ODI Series")

main2()