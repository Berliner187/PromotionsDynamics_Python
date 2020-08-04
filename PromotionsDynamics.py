import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

Promotions_Tesla = 'https://bcs-express.ru/kotirovki-i-grafiki/tsla'
Promotions_AMD = 'https://bcs-express.ru/kotirovki-i-grafiki/amd'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://bcs-express.ru/kotirovki-i-grafiki/aapl'
Promotions_IBM = 'https://bcs-express.ru/kotirovki-i-grafiki/ibm'
Promotions_Microsoft = 'https://bcs-express.ru/kotirovki-i-grafiki/msft'
Promotions_Yandex_Finam = 'https://www.finam.ru/quote/moex-akcii/pllc-yandex-n-v/'
Promotions_Yandex_Investing = 'https://ru.investing.com/equities/yandex'
Promotions_Google = 'https://ru.investing.com/equities/google-inc'

Valute_Bitcoin = 'https://www.investing.com/crypto/bitcoin'
Valute_Dollar = 'https://bcs-express.ru/kotirovki-i-grafiki/usd000utstom'

change = input('Валюты, Криптовалюты, IT-компании, Автопроизодители: ')

if change == '1':
    valute = input('Выберите валюту: ')

    if valute == '1':
        def check_currency_Dollar():
            full_page = requests.get(Valute_Dollar, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
            print("Текущий курс Доллара: " + convert[0].text + " Rub")

            convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
            print("Изменение составило: " + convert_dyn[0].text)

            dol = {'Курс сегодня: ', convert[0].text}
            dol.to_excel('../Документы/')

            check_currency_Dollar()
        check_currency_Dollar()


elif change == '2':
    auto = input('(Tesla) Выберите автопроизводителя: ')
    if auto == 'Tesla':
        def check_currency_Tesla():
            full_page = requests.get(Promotions_Tesla, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
            print("Текущая стоимость акций Tesla: " + convert[0].text + " $")
            time.sleep(4)
            check_currency_Tesla()
        check_currency_Tesla()

elif change == '3':
    IT = input('(AMD, Intel, Apple, IBM, Microsoft, Google, Yandex) Выберите IT-компанию: ')
    if IT == '1':
        def check_currency_AMD():
            full_page = requests.get(Promotions_AMD, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert_usd = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
            print("Текущая стоимость акций AMD: " + convert_usd[0].text + " $")

            convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
            print("Изменение составило: " + convert_dyn[0].text)

            time.sleep(10)
            check_currency_AMD()
        check_currency_AMD()

    elif IT == '2':
        def check_currency_Intel():
            full_page = requests.get(Promotions_Intel, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
            print("Текущая стоимость акций Intel: " + convert[0].text + " $")

            time.sleep(4)
            check_currency_Intel()
        check_currency_Intel()

    elif IT == '3':
        def check_currency_Apple():

            full_page = requests.get(Promotions_Apple, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
            print("Текущая стоимость акций Apple: " + convert[0].text + " $")
            time.sleep(5)
            check_currency_Apple()
        check_currency_Apple()

    elif IT == '4':
        def check_currency_IBM():

            full_page = requests.get(Promotions_IBM, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert_usd = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
            print("Текущая стоимость акций IBM: " + convert_usd[0].text + " $")

            convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
            print("Изменение составило: " + convert_dyn[0].text)

            time.sleep(10)
            check_currency_IBM()
        check_currency_IBM()

    elif IT == '5':
        def check_currency_Microsoft():
            full_page = requests.get(Promotions_Microsoft, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll("div", {"class": "quote-head__price-value js-quote-head-price js-price-close"})
            print("Текущая стоимость акций Microsoft: " + convert[0].text + " $")

            convert_dyn = soup.findAll("div", {"class": "quote-head__price-change js-profit-percent"})
            print("Изменение составило: " + convert_dyn[0].text)

            time.sleep(10)
            check_currency_Microsoft()
        check_currency_Microsoft()

    elif IT == '6':
        def check_currency_Google():

            full_page = requests.get(Promotions_Google, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-6369-last"})
            print("Текущая стоимость акций Google: " + convert_usd[0].text + " $")

            time.sleep(5)
            check_currency_Google()
        check_currency_Google()

    elif IT == '7':
        yan = input('Источник: ')
        if yan == '1':
            def check_currency_Yandex_Finam():

                full_page = requests.get(Promotions_Yandex_Finam, headers=headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')

                convert = soup.findAll("span", {"class": "PriceInformation__price--26G"})
                print("Текущая стоимость акций Яндекс: " + convert[0].text)
                time.sleep(5)
                check_currency_Yandex_Finam()
            check_currency_Yandex_Finam()

        elif yan == '2':
            def check_currency_Yandex_Investing():

                full_page = requests.get(Promotions_Yandex_Investing, headers=headers)
                soup = BeautifulSoup(full_page.content, 'html.parser')

                convert = soup.findAll("span", {"class": "arial_26 inlineblock pid-13999-last"})
                print("Текущая стоимость акций Яндекс: " + convert[0].text)

                convert_dyn = soup.findAll("span", {"class": "arial_20  pid-13999-pcp parentheses redFont"})
                print("Изменение составило: " + convert_dyn[0])

                time.sleep(5)
                check_currency_Yandex_Investing()
            check_currency_Yandex_Investing()

elif change =='4':
    crypto = input('Выберите крипту: ')
    if crypto == 'Bitcoin':
        def check_currency_Bitcoin():

            full_page = requests.get(Valute_Bitcoin, headers=headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')

            convert = soup.findAll("span", {"class": "pid-1057391-last"})
            print("Текущая стоимость Bitcoin: " + convert[0].text + " $")
            time.sleep(4)
            check_currency_Bitcoin()
        check_currency_Bitcoin()

else:
    print('Такого направления тут нет, буржуй')
    nachen = input('Press any key: ')
