from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://hastalarsoruyor.com/soru-lar/liste?type=&category=&sayfa={}'
links = []
titles = []
questions_body = []
answers = []
doctors_json = {}

# get the links of questions

for i in range(1,31):
    conn = requests.get(url.format(i))
    soup = BeautifulSoup(conn.content,'html5lib')
    
    q_body = soup.findAll('div',{'class':'question-body'})
    for q in q_body:
        links.append(q.a['href'])

# loop through links to get the title, question body, and answers

print(len(links))
for i in range(len(links)):
    soup1 = BeautifulSoup(requests.get(links[i]).content,'html5lib')
    ans_num = soup1.find('h3',{'class','section-box-title'})
    if ans_num and int(ans_num.text[-2]) > 0:
        answer_body = soup1.findAll('div',{'class','question-card'})
        if len(answer_body) > 1:

            title = soup1.findAll('h1',{'class','question-title'})
            if len(title) > 0:
                titles.append(title[0].text)
            
            body = soup1.findAll('p',{'class','question-desc'})
            if len(body) > 0:
                questions_body.append(body[0].text)

            print(len(answer_body))
            print('scrapping........')
            answer = answer_body[1].find('div',{'class','question-body'}).p.text
            answers.append(answer)

data = pd.DataFrame()

print(f'titles: {len(titles)}')
print(f'questions_body: {len(questions_body)}')
print(f'answers: {len(answers)}')
data['title'] = titles
data['questions'] = questions_body
data['answers'] = answers

data.head(10)
data.to_csv('hastalar_soruyor.csv')