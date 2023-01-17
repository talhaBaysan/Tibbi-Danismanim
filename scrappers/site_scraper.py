import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://www.doktorumonline.net'
start_url = 'https://www.doktorumonline.net/danisma-hatti/p/'
url = 'https://www.doktorumonline.net/danisma-hatti/p/{}'

conn = requests.get(url)

soup = BeautifulSoup(conn.content,'html5lib')

pages = int(soup.select("ul.pagination li")[-2].text)

links = []
containers = soup.select('div.question-item-container')
for cont in containers:
    link_div = cont.findAll('div',{'class':'button-item-container'})
    for l in link_div:
        links.append(l.a['href'])
    


for i in range(2,pages+1):
    containers = soup.select('div.question-item-container')
    for cont in containers:
        link_div = cont.findAll('div',{'class':'button-item-container'})
        for l in link_div:
            links.append(l.a['href'])

titles = []
questions_body = []
answers = []
doctors_json = {}

for i in range(len(links)):
    soup1 = BeautifulSoup(requests.get(base_url + links[i]).content,'html5lib')
    
    # finding title
    title = soup1.findAll('h1',{'itemprop','question-title'})
    if title:
        titles.append(title[0].text)
        # finding question body and answer
        questions_body = soup1.findAll('p',{'itemprop':'text'})
        print(f'adding to array.....{links[i]}')
        # print(questions_body[1].text)
        questions_body.append(questions_body[0].text)
        answers.append(questions_body[1].text)
    
    # doctors_json[i] = {}
    # doctors_json[i]['title'] = title[0].text
    # doctors_json[i]['questions_body'] = questions_body[0].text
    # doctors_json[i]['answer'] = questions_body[1].text


data = pd.DataFrame()
data['title'] = titles
data['answers'] = answers

data.to_csv('doktoronline.csv')
# import json

# with open('doctoronline.json','w', encoding='utf-8') as file:
#     json.dump(doctors_json,file,ensure_ascii=False)



