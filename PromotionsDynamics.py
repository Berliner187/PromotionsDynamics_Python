import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

Promotions_Tesla = 'https://m.ru.investing.com/equities/tesla-motors'
Promotions_AMD = 'https://www.google.com/search?q=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+amd&oq=%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+&aqs=chrome.0.69i59j69i57j0l3j69i61l3.2520j1j7&sourceid=chrome&ie=UTF-8'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://ru.investing.com/equities/apple-computer-inc'
Promotions_IBM = 'https://ru.investing.com/equities/ibm'
Promotions_Microsoft = 'https://ru.investing.com/equities/microsoft-corp'
Promotions_Yandex = 'https://www.finam.ru/quote/moex-akcii/pllc-yandex-n-v/'
Promotions_Bitcoin = 'https://www.investing.com/crypto/bitcoin'

inp = input('Tesla, Apple, IBM, Microsoft, Yandex, Bitcoin, Intel, AMD: ')

if inp == 'Tesla':

    def check_currency_Tesla():
        full_page = requests.get(Promotions_Tesla, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "Promotions_Tesla = 'lastInst pid-13994-last"})
        print("Текущая стоимость акций Tesla: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_Tesla()
    check_currency_Tesla()

elif inp == 'AMD':

    def check_currency_AMD():
        full_page = requests.get(Promotions_AMD, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "IsqQVc NprOob XcVN5d"})
        print("Текущая стоимость акций AMD: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_AMD()
    check_currency_AMD()

elif inp == 'Intel':

    def check_currency_Intel():

        full_page = requests.get(Promotions_Intel, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser' + " $")

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
        print("Текущая стоимость акций Intel: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_Intel()
    check_currency_Intel()

elif inp == 'Apple':

    def check_currency_Apple():

        full_page = requests.get(Promotions_Apple, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
        print("Текущая стоимость акций Apple: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_Apple()
    check_currency_Apple()

elif inp == 'IBM':

    def check_currency_IBM():

        full_page = requests.get(Promotions_IBM, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8082-last"})
        print("Текущая стоимость акций IBM: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_IBM()
    check_currency_IBM()

elif inp == 'Microsoft':

    def check_currency_Microsoft():

        full_page = requests.get(Promotions_Microsoft, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-252-last"})
        print("Текущая стоимость акций Microsoft: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_Microsoft()
    check_currency_Microsoft()

elif inp == 'Yandex':

    def check_currency_Yandex():

        full_page = requests.get(Promotions_Yandex, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "PriceInformation__price--26G"})
        print("Текущая стоимость акций Яндекс: " + convert[0].text)
        time.sleep(5)
        check_currency_Yandex()
    check_currency_Yandex()

elif inp == 'Bitcoin':

    def check_currency_Bitcoin():

        full_page = requests.get(Promotions_Bitcoin, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "pid-1057391-last"})
        print("Текущая стоимость Bitcoin: " + convert[0].text + " $")
        time.sleep(4)
        check_currency_Bitcoin()
    check_currency_Bitcoin()

else:
    print('Такой компании тут нет, буржуй')
    nachen = input('Press any key: ')