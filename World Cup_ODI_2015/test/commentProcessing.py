from jinja2._compat import izip

def main():
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/753287.html"
    # content(theurl)
    line_number = 1
    s1 = ""
    I=1
    x=list()
    level=list()
    isCommentContinuing=0
    temp=0
    commentSoFar=list()
    with open('ODIComment-With-Hader2.txt', encoding='ISO-8859-1') as a_file,open('ODIDate-With-Hader2.txt', encoding='ISO-8859-1') as b_file:
        Comment= ""
        import openpyxl
        wb = openpyxl.load_workbook('comment1.xlsx')
        sheet = wb.active
        target = open("WroldcupComment.txt", 'a')
        # for a_line, b_line in izip(a_file,b_file):
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s = a_line.rstrip()
            if (s.isdigit()):
                if(Comment!=""):
                    # print(Comment)
                    # print()
                    # if(temp==1):
                    temp=1
                    Comment = Comment.strip()
                    Comment = Comment.rstrip()
                    for s in commentSoFar:
                        if Comment in s:
                            temp=0
                            break
                    if (temp==1):
                        # Comment = Comment.strip()
                        # Comment = Comment.rstrip()
                        # x.add(Comment)
                        x.append(Comment)
                        level.append(Label)
                        if(len(commentSoFar)>=20):
                            commentSoFar.pop(0)


                        print(len(commentSoFar))
                        commentSoFar.append(Comment)
                        print(Comment)
                        print()
                            # commentSoFar.clear()
                    # else:
                    #     Comment = Comment.strip()
                    #     Comment = Comment.rstrip()
                    #     x.add(Comment)
                    #     print(Comment)
                    #     print()
                    # target.write(Comment)
                    # target.write('\n\n')
                    I+=1
                isCommentContinuing=0
                Comment = ""

                # print("Its a digit: " + s)
            elif (s.startswith("Label")):
                # print("Its lable "+s)
                label=s.split(":")
                Label=label[1].strip()
                # print(Label)

            elif (s != ""):
                Comment += s
                # isCommentContinuing=1
                # if(temp==1):
                #     commentSoFar.add(s)

            # elif (Comment == ""):
            #     if (isCommentContinuing):
            #         temp=1
            #     # print(Comment)
            #     # print()
            #     target.write(Comment)
            #     sheet["A" + str(I)] = Comment
            #     # Comment = ""
            #     # I += 1
            # if (I == 33):
            #      break
        # wb.save('comment.xlsx')
    print(len(x))
    print
    print(len(level))
    # lst=list(x)
    I=1
    for s in x:
        # target.write(s)
        # target.write('\n\n')
        sheet["A" + str(I)] = s
        I+=1
    I = 1
    for s in level:
        # target.write(s)
        # target.write('\n\n')
        sheet["B" + str(I)] = s
        I += 1
    wb.save('comment1.xlsx')

main()