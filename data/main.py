import pandas as pd
import re

data1 = pd.read_csv('doktor_evi.csv',encoding='utf-8')
data2 = pd.read_csv('doktoronline.csv',encoding='utf-8')
data3 = pd.read_csv('hastalar_soruyor.csv',encoding='utf-8')
data4 = pd.read_excel('../uzmanim/veri_setleri/veriseti.xls')
titles = []
answers = []

for item in data1['title'].values:
    item = re.sub('Soru:\d+.\d+.\d+','',item)
    item = re.sub('Örn Soru \d+:','',item)
    titles.append(item)
    
for item in data2['title'].values:
    item = re.sub('Soru:\d+.\d+.\d+','',item)
    item = re.sub('Örn Soru \d+:','',item)
    titles.append(item)
for item in data3['title'].values:
    item = re.sub('Soru:\d+.\d+.\d+','',item)
    item = re.sub('Örn Soru \d+:','',item)
    titles.append(item)

for item in data4['Questions'].values:
    titles.append(item)


for item in data1['answers'].values:
    answers.append(item)

for item in data2['answers'].values:
    answers.append(item)

for item in data3['answers'].values:
    answers.append(item)

for item in data4['Answers'].values:
    answers.append(item)

main_data = pd.DataFrame()

main_data['questions'] = titles
main_data['answers'] = answers


main_data.to_excel('main_data.csv',encoding='utf-8')

