from thefuzz import fuzz
from similarity import return_the_most_similar  
import xlrd

def thefuzzmatching(sickness,questions): #fuzzyStringMatching kütüphanesinin benzerlik fonksiyonundan yararlanan fonksiyon
    max = fuzz.ratio(sickness,questions[0])
    index = 0
    index_counter = 1
    for i in questions:
        temp = fuzz.ratio(sickness,i)
        if(temp > max):
            max = temp
            index = index_counter
        index_counter = index_counter + 1 
    
    return index #en benzer sorunun indexi

#bazı test cümleleri,sorguları
test = ["başım ağrıyor","ailemle anlaşamıyorum","kulaklarımda çınlama hissi var","kulağımda basınç hissediyorum","aşı olmaktan korkuyorum","çok unutkanım","ani sinir patlaması yaşıyorum",
"çok agresifim","yalnız hissediyorum","göğsümde bir ağrı var","hayatım çok stresli","uyuyamıyorum","kekeliyorum","sürekli halsizim","sinüzit","burun kemiğim eğri",
"ses kısıklığı var","uykumda kendi kendime konuşuyorum","dikkat eksikliği ve konstantrasyon eksikliği","öğrenmekten zorlanıyorum bir şeyi çok zor öğreniyorum"]

wb = xlrd.open_workbook("./data/main_data_60.xls") #veri setini okuyorum
sheet = wb.sheet_by_index(0)
questions = [] #questions adlı diziye soruları kopyalanıyor
for i in range (1,sheet.nrows):
    questions.append(sheet.cell_value(i, 0).lower())

rate=0
for string in test: #iki fonksiyonun bulduğu sonuçları karşılaştırıp benzerlik oranını hesaplanıyor
    if(thefuzzmatching(string,questions) == return_the_most_similar(string,questions)):
        rate = rate + 1

print(f"sistemin doğruluk oranı %{rate * 5}")