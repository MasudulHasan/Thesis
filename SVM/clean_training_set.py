import openpyxl

def main():
    TotalCount=0
    wb = openpyxl.load_workbook('~1k comments.xlsx')
    sheet = wb.active

    reqd_ids = []
    while TotalCount < sheet.max_row:
        print(TotalCount)
        TotalCount += 1
        comment = sheet["A" + str(TotalCount)].value
        if(len(comment.split()) <= 2):
            reqd_ids += [str(TotalCount)]
            # print("GHAPLA: " + TotalCount)


    print(' '.join(reqd_ids))

main()