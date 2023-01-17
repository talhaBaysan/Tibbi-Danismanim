from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = 'https://doktorevi.com/soru'
start_url = 'https://doktorevi.com/soru-cevap/page/{}'

conn = requests.get(base_url)
soup = BeautifulSoup(conn.content,'html5lib')

links = []
titles = []
questions = []
answers = []

questions_container = soup.find('div',{'class','dwqa-questions-list'})
questions = questions_container.findAll('div',{'class','dwqa-status-answered'})

for q in questions:
    links.append(q.header.a['href'])
    # titles.append(q.header.a.text)

for i in range(2,11):
    soup1 = BeautifulSoup(requests.get(start_url.format(i)).content,'html5lib')
    questions_container = soup.find('div',{'class','dwqa-questions-list'})
    questions = questions_container.findAll('div',{'class','dwqa-status-answered'})

    for q in questions:
        links.append(q.header.a['href'])
        # titles.append(q.header.a.text)

to_remove = []
for i in range(len(links)):
    soup2 = BeautifulSoup(requests.get(links[i]).content,'html5lib')
    
    answer_body = soup2.find('div',{'class','dwqa-answer-content'})
    if answer_body:
        print(f'Scrapping from link: {links[i]}')
        title_body = soup2.find('span',{'class','dwqa-current'})
        titles.append(title_body.text)

        answers.append(answer_body.p.text)
 
data = pd.DataFrame()

print(f'titles: {len(titles)}')
# print(f'questions_body: {len(questions)}')
print(f'answers: {len(answers)}')
data['title'] = titles
# data['questions'] = questions
data['answers'] = answers

print(data.head(10))
data.to_csv('doktor_evi.csv')