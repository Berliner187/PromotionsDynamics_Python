import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

Promotions_Tesla = 'https://ru.investing.com/equities/tesla-motors'
Promotions_AMD = 'https://ru.investing.com/equities/adv-micro-device'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://ru.investing.com/equities/apple-computer-inc'
Promotions_IBM = 'https://ru.investing.com/equities/ibm'
Promotions_Microsoft = 'https://ru.investing.com/equities/microsoft-corp'

inp = input('Tesla, Apple, IBM, Microsoft, Intel или AMD? ')

if inp == 'Tesla':

    def check_currency_Tesla():
        full_page = requests.get(Promotions_Tesla, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13994-last"})
        print("Текущая стоимость акций Tesla: " + convert[0].text + " $")
        time.sleep(1)
        check_currency_Tesla()
    check_currency_Tesla()

elif inp == 'AMD':

    def check_currency_AMD():
        full_page = requests.get(Promotions_AMD, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
        print("Текущая стоимость акций AMD: " + convert[0].text + " $")
        time.sleep(1)
        check_currency_AMD()
    check_currency_AMD()

elif inp == 'Intel':

    def check_currency_Intel():

        full_page = requests.get(Promotions_Intel, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser' + " $")

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
        print("Текущая стоимость акций Intel: " + convert[0].text + " $")
        time.sleep(1)
        check_currency_Intel()
    check_currency_Intel()

elif inp == 'Apple':

    def check_currency_Apple():

        full_page = requests.get(Promotions_Apple, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
        print("Текущая стоимость акций Apple: " + convert[0].text + " $")
        time.sleep(1)
        check_currency_Apple()
    check_currency_Apple()

elif inp == 'IBM':

    def check_currency_IBM():

        full_page = requests.get(Promotions_IBM, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8082-last"})
        print("Текущая стоимость акций IBM: " + convert[0].text + " $")
        time.sleep(1)
        check_currency_IBM()
    check_currency_IBM()

elif inp == 'Microsoft':

    def check_currency_Microsoft():

        full_page = requests.get(Promotions_Microsoft, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-252-last"})
        print("Текущая стоимость акций Microsoft: " + convert[0].text + " $")
        time.sleep(1)
        check_currency_Microsoft()
    check_currency_Microsoft()

else:
    print('Такой компании тут нет, буржуй')
    nachen = input('Press any key: ')
