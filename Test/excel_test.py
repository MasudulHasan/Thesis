import openpyxl

def main():
    wb = openpyxl.Workbook()
    sheet = wb.active
    for i in range(1, 6):
        sheet["A"+str(i)] = "A test"
        sheet["B"+str(i)] = "B test"
        sheet["C"+str(i)] = "C test"
        sheet["D"+str(i)] = "D test"

    wb.save('excel_test.xlsx')

main()