import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

Promotions_Tesla = 'https://bcs-express.ru/kotirovki-i-grafiki/tsla'
Promotions_AMD_reserve = 'https://bcs-express.ru/kotirovki-i-grafiki/amd'
Promotions_AMD = 'https://www.investing.com/equities/adv-micro-device'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://www.investing.com/equities/apple-computer-inc'
Promotions_IBM = 'https://www.investing.com/equities/ibm'
Promotions_Microsoft = 'https://www.investing.com/equities/microsoft-corp'
Promotions_Yandex = 'https://www.investing.com/equities/yandex'
Promotions_Google = 'https://ru.investing.com/equities/google-inc'
Promotions_Facebook = 'https://www.investing.com/equities/facebook-inc'

Valute_Bitcoin = 'https://www.investing.com/crypto/bitcoin'
Valute_Dollar = 'https://bcs-express.ru/kotirovki-i-grafiki/usd000utstom'
Valute_Euro = 'https://ru.investing.com/currencies/eur-rub'

update_text = '********************************* Обновление данных *********************************'

def check_Vatute():
    print()
    print('******* Доллар *******')
    full_page = requests.get(Valute_Dollar, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущий курс Доллара: " + convert[0].text + " ₽")
    convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
    print("Изменение составило: " + convert_dyn[0].text)
    time.sleep(2)

    print('******* Евро *******')
    full_page = requests.get(Valute_Euro, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-1691-last"})
    print("Текущий курс Евро: " + convert[0].text + " ₽")
    print(update_text)
    time.sleep(2)
    check_Vatute()

def check_Crypto():

    full_page = requests.get(Valute_Bitcoin, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "pid-1057391-last"})
    print("Текущая стоимость Bitcoin: " + convert[0].text + " $")
    time.sleep(2)
    print(update_text)
    check_Crypto()

def check_Auto():
    full_page = requests.get(Promotions_Tesla, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
    print("Текущая стоимость акций Tesla: " + convert[0].text + " $")
    print(update_text)
    time.sleep(2)
    check_Auto()

def check_IT():
    print()
    print('**************** AMD ****************')    
    full_page = requests.get(Promotions_AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
    print("Текущая стоимость акций AMD: " + convert_usd[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-8274-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-8274-high"})
    print("Дневной минимум: " + convert_min[0].text)
    print("Дневной максимум: " + convert_max[0].text)
    print()
    time.sleep(2)

    print('**************** Intel ****************')
    full_page = requests.get(Promotions_Intel, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
    print("Текущая стоимость акций Intel: " + convert[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-251-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-251-high"})
    print("Дневной минимум: " + convert_min[0].text)
    print("Дневной максимум: " + convert_max[0].text)
    print()
    time.sleep(2)

    print('**************** Apple ****************')
    full_page = requests.get(Promotions_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
    print("Текущая стоимость акций Apple: " + convert[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-6408-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-6408-high"})
    print("Дневной минимум: " + convert_min[0].text + " $")
    print("Дневной максимум: " + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** IBM ****************')
    full_page = requests.get(Promotions_IBM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-8082-last"})
    print("Текущая стоимость акций IBM: " + convert_usd[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-8082-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-8082-high"})
    print("Дневной минимум: " + convert_min[0].text + " $")
    print("Дневной максимум: " + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Microsoft ****************')
    full_page = requests.get(Promotions_Microsoft, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-252-last"})
    print("Текущая стоимость акций Microsoft: " + convert[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-252-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-252-high"})
    print("Дневной минимум: " + convert_min[0].text + " $")
    print("Дневной максимум: " + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Google ****************')
    full_page = requests.get(Promotions_Google, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-6369-last"})
    print("Текущая стоимость акций Google: " + convert_usd[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-6369-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-6369-high"})
    print("Дневной минимум: " + convert_min[0].text + " $")
    print("Дневной максимум: " + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Facebook ****************')
    full_page = requests.get(Promotions_Facebook, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-26490-last"})
    print("Текущая стоимость акций Facebook: " + convert_usd[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-26490-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-26490-high"})
    print("Дневной минимум: " + convert_min[0].text + " $")
    print("Дневной максимум: " + convert_max[0].text + " $")
    print()
    time.sleep(2)

    print('**************** Yandex ****************')
    full_page = requests.get(Promotions_Yandex, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13999-last"})
    print("Текущая стоимость акций Яндекс: " + convert[0].text + " $")
    convert_min = soup.findAll("span", {"class": "inlineblock pid-13999-low"})
    convert_max = soup.findAll("span", {"class": "inlineblock pid-13999-high"})
    print("Дневной минимум: " + convert_min[0].text + " $")
    print("Дневной максимум: " + convert_max[0].text + " $")
    print(update_text)
    time.sleep(2)
    print()
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
