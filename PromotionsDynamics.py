import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

Promotions_Tesla = 'https://bcs-express.ru/kotirovki-i-grafiki/tsla'
Promotions_AMD = 'https://bcs-express.ru/kotirovki-i-grafiki/amd'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://www.investing.com/equities/apple-computer-inc'
Promotions_IBM = 'https://bcs-express.ru/kotirovki-i-grafiki/ibm'
Promotions_Microsoft = 'https://bcs-express.ru/kotirovki-i-grafiki/msft'
Promotions_Yandex = 'https://ru.investing.com/equities/yandex'
Promotions_Google = 'https://ru.investing.com/equities/google-inc'

Valute_Bitcoin = 'https://www.investing.com/crypto/bitcoin'
Valute_Dollar = 'https://bcs-express.ru/kotirovki-i-grafiki/usd000utstom'
Valute_Euro = 'https://ru.investing.com/currencies/eur-rub'

def check_Vatute():
    full_page = requests.get(Valute_Dollar, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущий курс Доллара: " + convert[0].text + " ₽")
    convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
    print("Изменение составило: " + convert_dyn[0].text)
    time.sleep(2)

    full_page = requests.get(Valute_Euro, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-1691-last"})
    print("Текущий курс Евро: " + convert[0].text + " ₽")
    print('Обновление данных...')
    time.sleep(2)
    check_Vatute()

def check_Crypto():
    full_page = requests.get(Valute_Bitcoin, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "pid-1057391-last"})
    print("Текущая стоимость Bitcoin: " + convert[0].text + " $")
    time.sleep(2)
    print('Обновление данных...')
    check_Crypto()

def check_Auto():
    full_page = requests.get(Promotions_Tesla, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущая стоимость акций Tesla: " + convert[0].text + " $")
    print('Обновление данных...')
    time.sleep(2)
    check_Auto()

def check_IT():
    full_page = requests.get(Promotions_AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущая стоимость акций AMD: " + convert_usd[0].text + " $")
    convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
    print("Изменение составило: " + convert_dyn[0].text)
    time.sleep(2)

    full_page = requests.get(Promotions_Intel, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
    print("Текущая стоимость акций Intel: " + convert[0].text + " $")
    time.sleep(2)

    full_page = requests.get(Promotions_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
    print("Текущая стоимость акций Apple: " + convert[0].text + " $")
    time.sleep(2)

    full_page = requests.get(Promotions_IBM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущая стоимость акций IBM: " + convert_usd[0].text + " $")
    convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
    print("Изменение составило: " + convert_dyn[0].text)
    time.sleep(2)

    full_page = requests.get(Promotions_Microsoft, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущая стоимость акций Microsoft: " + convert[0].text + " $")
    convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
    print("Изменение составило: " + convert_dyn[0].text)
    time.sleep(2)

    full_page = requests.get(Promotions_Google, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-6369-last"})
    print("Текущая стоимость акций Google: " + convert_usd[0].text + " $")
    time.sleep(2)

    full_page = requests.get(Promotions_Yandex, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13999-last"})
    print("Текущая стоимость акций Яндекс: " + convert[0].text + " $")
    time.sleep(2)
    print('Обновление данных...')
    check_IT()

print('Выберите направление цифрой: ')
change_Prom = input('1 - Валюты, 2 - Криптовалюты, 3 - Автопроизодители, 4 - IT-корпорации: ')

if change_Prom == '1':
    check_Vatute()
elif change_Prom == '2':
    check_Crypto()
elif change_Prom == '3':
    check_Auto()
elif change_Prom == '4':
    check_IT()
else:
    print('Такого направления нет, повторите ввод перезапуском программы')
