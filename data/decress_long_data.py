import xlrd
import xlwt
from xlwt import Workbook

# sorular içinden 60 kelimeden kısa olanları excelle  
wb1 = Workbook()
sheet1 = wb1.add_sheet('Sheet 1')
sheet1.write(0,0,"Questions")
sheet1.write(0,1,"Answers")

# var olan excell'i okumak için
wb = xlrd.open_workbook("main_data.xls")
sheet = wb.sheet_by_index(0)

j=1
for i in range (1,sheet.nrows):
    # sorunun kelime sayısını hesaplayıp eğer 60'dan küçük ise yeni excell'e yazılıyor
    words = str(sheet.cell_value(i, 0)).split()
    if(len(words) <= 60):
        sheet1.write(j,0,sheet.cell_value(i, 0).lower())
        sheet1.write(j,1,sheet.cell_value(i, 1).lower())
        j = j + 1 
wb1.save("main_data_60.xls") #yeni excell dosyası.