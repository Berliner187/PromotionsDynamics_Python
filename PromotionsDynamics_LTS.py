#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
headers_Win = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

Promotions_Tesla = 'https://ru.investing.com/equities/tesla-motors'
Promotions_Nissan = 'https://ru.investing.com/equities/nissan-motor-co.,-ltd.'
Promotions_AMD_reserve = 'https://bcs-express.ru/kotirovki-i-grafiki/amd'
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

Valute_Bitcoin = 'https://www.investing.com/crypto/bitcoin'
Valute_Dollar_reserve = 'https://bcs-express.ru/kotirovki-i-grafiki/usd000utstom'
Valute_Dollar = 'https://ru.investing.com/currencies/usd-rub'
Valute_Euro = 'https://ru.investing.com/currencies/eur-rub'

update_text = '------------------------------- Update Data... -------------------------------'
currency_now = 'Current course '
promotions_now = 'Current value of shares'
day_min = 'Daily low: '
day_max = 'Daily maximum: '

def check_Vatute():
    print()
    print('******* Dollar *******')
    full_page = requests.get(Valute_Dollar, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-2186-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-2186-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-2186-high"})
    print(currency_now + "Dollar: " + convert[0].text + " ₽")
    print(day_min + convert_min[0].text + " ₽")
    print(day_max + convert_max[0].text + " ₽")
    print()
    time.sleep(2)

    print('******* Euro *******')
    full_page = requests.get(Valute_Euro, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-1691-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-1691-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-1691-high"})
    print(currency_now + convert[0].text + " ₽")
    print(day_min + convert_min[0].text + " ₽")
    print(day_max + convert_max[0].text + " ₽")
    print(update_text)
    time.sleep(2)
    check_Vatute()
    print()

def check_Crypto():
    print()
    print('******* Bitcoin *******')
    full_page = requests.get(Valute_Bitcoin, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "pid-1057391-last"})
    convert_min = soup.findAll("span", {"class": ""})
    convert_max = soup.findAll("span", {"class": ""})
    print("Текущая стоимость Bitcoin: " + convert[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    print(update_text)
    time.sleep(2)
    check_Crypto()

def check_Auto():
    print()
    print('******* Tesla *******')
    full_page = requests.get(Promotions_Tesla, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13994-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-13994-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-13994-high"})
    print(promotions_now + " Tesla: " + convert[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    time.sleep(2)
    print()

    print('******* Nissan *******')
    full_page = requests.get(Promotions_Nissan, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-44127-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-44127-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-44127-high"})
    print(promotions_now + " Nissan: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('******* General Motors *******')
    full_page = requests.get(Promotions_GM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-239-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-239-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-239-high"})
    print(promotions_now + " General Motors: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('******* Ford *******')
    full_page = requests.get(Promotions_Ford, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-255-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-255-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-255-high"})
    print(promotions_now + " Ford: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('******* Daimler AG *******')
    full_page = requests.get(Promotions_Daimler, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-355-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-355-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-355-high"})
    print(promotions_now + " Ford: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)
    print(update_text)
    check_Auto()    

def check_IT():
    print()
    print('**************** AMD ****************')    
    full_page = requests.get(Promotions_AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-8274-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-8274-high"})
    print(promotions_now + " AMD: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text)
    print(day_max + convert_max[0].text)
    print()
    time.sleep(2)

    print('**************** Intel ****************')
    full_page = requests.get(Promotions_Intel, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-251-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-251-high"})
    print(promotions_now + " Intel: " + convert[0].text + " $")
    print(day_min + convert_min[0].text)
    print(day_max + convert_max[0].text)
    print()
    time.sleep(2)

    print('**************** Apple ****************')
    full_page = requests.get(Promotions_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-6408-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-6408-high"})
    print(promotions_now + " Apple: " + convert[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** IBM ****************')
    full_page = requests.get(Promotions_IBM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-8082-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-8082-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-8082-high"})
    print(promotions_now + " IBM: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Microsoft ****************')
    full_page = requests.get(Promotions_Microsoft, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-252-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-252-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-252-high"})
    print(promotions_now + " Microsoft: " + convert[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Google ****************')
    full_page = requests.get(Promotions_Google, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-6369-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-6369-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-6369-high"})
    print(promotions_now + " Google: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Facebook ****************')
    full_page = requests.get(Promotions_Facebook, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-26490-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-26490-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-26490-high"})
    print(promotions_now + " Facebook: " + convert_usd[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Yandex ****************')
    full_page = requests.get(Promotions_Yandex, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13999-last"})
    convert_min = soup.findAll("span", {"class": "inlineblock pid-13999-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-13999-high"})
    print(promotions_now + " Яндекс: " + convert[0].text + " $")
    print(day_min + convert_min[0].text + " $")
    print(day_max + convert_max[0].text + " $")

    print()
    print(update_text)
    check_IT()

print('Change direction numeral: ')
change_Prom = input('1 - Currency, 2 - Cryptocurrencies, 3 - Car manufacturers, 4 - IT-corporations: ')

if change_Prom == '1':
    check_Vatute()
elif change_Prom == '2':
    check_Crypto()
elif change_Prom == '3':
    check_Auto()
elif change_Prom == '4':
    check_IT()
else:
    print('Error #355, please try again on restart ')
