from tkinter import Text
import PySimpleGUI as sg
import pandas as pd
from similarity import return_the_most_similar

# excell dosyası okuma 
data = pd.read_excel('./data/main_data_60.xls')

questions = list(data['Questions'].values) # sorular listesi
answers = list(data['Answers'].values) # cevaplar listesi

for i in range(len(questions)):
    questions[i] = questions[i].lower()
    answers[i] = answers[i].lower()

# arayüz bilişenleri
sg.theme('DarkTeal9')

sickness = [
    [sg.Text('Şikayetinizi kısaca anlatınız:')],
    [sg.InputText(key="-IN-")],
    [sg.OK(key='-OK-'),sg.Button('Çık',key='-CLOSE-')]
]

diagnose = [[sg.Multiline("Şikayetiniz nedir?", size=(45,15),key="-DIAGNOSE-")]]

layout = [
    [
        sg.Column(sickness),
        sg.VSeperator(),
        sg.Column(diagnose),
    ]
]

window = sg.Window(title="Tıbbi Danışmanlığı", layout= layout, margins=(70, 70))

while True:
    event, values = window.read() 
    if event == "-OK-":
        text_input = values['-IN-']
        window['-DIAGNOSE-'].update(answers[(return_the_most_similar(text_input.lower(),questions))-1])
    if event=="-CLOSE-" or event == sg.WIN_CLOSED:
        break
window.close()