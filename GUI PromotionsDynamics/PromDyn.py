#!/usr/bin/env python3
import eel
import requests
from bs4 import BeautifulSoup


eel.init("web")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

Promotions_Tesla = 'https://ru.investing.com/equities/tesla-motors'
Promotions_Nissan = 'https://ru.investing.com/equities/nissan-motor-co.,-ltd.'
Promotions_AMD = 'https://www.investing.com/equities/adv-micro-device'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://www.investing.com/equities/apple-computer-inc'
Promotions_IBM = 'https://www.investing.com/equities/ibm'
Promotions_Microsoft = 'https://www.investing.com/equities/microsoft-corp'
Promotions_Yandex = 'https://www.investing.com/equities/yandex'
Promotions_Google = 'https://ru.investing.com/equities/google-inc'
Promotions_Facebook = 'https://www.investing.com/equities/facebook-inc'
Promotions_GM = 'https://ru.investing.com/equities/gen-motors'
Promotions_Ford = 'https://ru.investing.com/equities/ford-motor-co'
Promotions_Daimler = 'https://ru.investing.com/equities/daimler'
Promotions_EA = 'https://ru.investing.com/equities/electronic-arts-inc'
Promotions_Huawei = 'https://www.investing.com/equities/huawei-culture'


@eel.expose
def check_AMD():
    full_page = requests.get(Promotions_AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
    output = convert[0].text
    print(output)
    return output

@eel.expose
def check_Intel():
    full_page = requests.get(Promotions_Intel, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
    output = convert[0].text
    return output

@eel.expose
def check_Apple():
    full_page = requests.get(Promotions_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
    output = convert[0].text
    print(output)
    return output

@eel.expose
def check_IBM():
    full_page = requests.get(Promotions_IBM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8082-last"})
    output = convert[0].text
    return output

@eel.expose
def check_Microsoft():
    full_page = requests.get(Promotions_Microsoft, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-252-last"})
    output = convert[0].text
    return output

@eel.expose
def check_Google():
    full_page = requests.get(Promotions_Google, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6369-last"})
    output = convert[0].text
    return output

@eel.expose
def check_Facebook():
    full_page = requests.get(Promotions_Facebook, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-26490-last"})
    output = convert[0].text
    return output

@eel.expose
def check_EA():
    full_page = requests.get(Promotions_EA, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6472-last"})
    output = convert[0].text
    return output

@eel.expose
def check_Yandex():
    full_page = requests.get(Promotions_Yandex, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13999-last"})
    output = convert[0].text
    return output

@eel.expose
def check_Huawei():
    full_page = requests.get(Promotions_Huawei, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-944369-last"})
    output = convert[0].text
    return output


@eel.expose
def check_gap_Apple():
    History_Apple = 'https://ru.investing.com/equities/apple-computer-inc-historical-data'
    full_page = requests.get(History_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_price = soup.findAll("td", {"class": "greenFont"})
    for total in range(0, 20, 2):
        price = convert_price[total].text
        print(price)




eel.start("PromDyn.html", size=(1400, 800))