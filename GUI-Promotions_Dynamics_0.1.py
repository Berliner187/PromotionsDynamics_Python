from tkinter import *
from functools import partial
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

Promotions_Apple = 'https://www.investing.com/equities/apple-computer-inc'
Promotions_AMD = 'https://ru.investing.com/equities/adv-micro-device'
root = Tk()
print('Программа запущена')

root['bg'] = '#fafafa'
root.title('Konverter Program')
root.geometry('700x600')
root.resizable(width=False, height=False)

Frame = Frame(root, bg='#fafafa')
Frame.place(relx=.05, rely=.05, relwidth=.9, relheight=.9)

title_text = Label(Frame, text='Динамика акций', bg='#fafafa',  font='Arial 24', width=100, height=2) 	# Титульный текст
title_text.pack()

def check_Apple():
    out = Label(Frame, text=' ', bg='#fafafa', width=40)  # Текст вывода
    out.pack()
    full_page = requests.get(Promotions_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
    apple_prom = convert[0].text
    apple_now = apple_prom
    out = Label(Frame, text=apple_now + ' $', bg='#fecc50', font='Arial 16', width=22)  # Текст вывода
    out.pack()

def check_AMD():
    out = Label(Frame, text=' ', bg='#fafafa', width=40)  # Текст вывода
    out.pack()
    full_page = requests.get(Promotions_AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
    amd_prom = convert[0].text
    amd_now = amd_prom
    out = Label(Frame, text=amd_now + ' $', bg='#fecc50', font='Arial 16', width=22)  # Текст вывода
    out.pack()

btn_apple = Button(Frame, text='Apple', command=check_Apple, font='Arial 14', bg='#fecc50', width=20)
btn_apple.pack()

none_text = Label(Frame, text=' ', bg='#fafafa', width=40)
none_text.pack()

btn_amd = Button(Frame, text='AMD', command=check_AMD, font='Arial 14', bg='#fecc50', width=20)
btn_amd.pack()


root.mainloop()
print('Программа остановлена')