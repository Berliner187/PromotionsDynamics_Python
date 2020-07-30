import requests
from bs4 import BeautifulSoup
import time

Promotions_Tesla = 'https://ru.investing.com/equities/tesla-motors'
Promotions_AMD = 'https://ru.investing.com/equities/adv-micro-device'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

inp = input('Tesla или AMD? ')
if inp == 'Tesla':

    def check_currency_Tesla():
        full_page = requests.get(Promotions_Tesla, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13994-last"})
        print("Текущая стоимость акций Tesla: " + convert[0].text)
        time.sleep(1)
        check_currency_Tesla()
    check_currency_Tesla()

elif inp == 'AMD':

    def check_currency_AMD():
        full_page = requests.get(Promotions_AMD, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
        print("Текущая стоимость акций AMD: " + convert[0].text)
        time.sleep(1)
        check_currency_AMD()
    check_currency_AMD()

else:
    print('С парашей, такой компании тут нет, буржуй')
    nachen = input('Press any key: ')