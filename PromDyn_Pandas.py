#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
from datetime import date

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
headers_Win = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

Promotions_Tesla = 'https://ru.investing.com/equities/tesla-motors'
Promotions_Nissan = 'https://ru.investing.com/equities/nissan-motor-co.,-ltd.'
Promotions_AMD = 'https://ru.investing.com/equities/adv-micro-device'
Promotions_Intel = 'https://ru.investing.com/equities/intel-corp'
Promotions_Apple = 'https://ru.investing.com/equities/apple-computer-inc'
Promotions_IBM = 'https://ru.investing.com/equities/ibm'
Promotions_Microsoft = 'https://ru.investing.com/equities/microsoft-corp'
Promotions_Yandex = 'https://ru.investing.com/equities/yandex'
Promotions_Google = 'https://ru.investing.com/equities/google-inc'
Promotions_Facebook = 'https://ru.investing.com/equities/facebook-inc'
Promotions_GM = 'https://ru.investing.com/equities/gen-motors'
Promotions_Ford = 'https://ru.investing.com/equities/ford-motor-co'
Promotions_Daimler = 'https://ru.investing.com/equities/daimler'

Valute_Bitcoin = 'https://ru.investing.com/crypto/bitcoin/btc-usd'
Valute_Dollar = 'https://ru.investing.com/currencies/usd-rub'
Valute_Euro = 'https://ru.investing.com/currencies/eur-rub'

start_collection = 'Data collection in progress, please wait'
progress_bar = 'Progress: '
packing = 'Packing into file...'
sheet_name = 'Данные рынка на '

prom_now = "Текущая стоимость акций "
prom_day_max = 'Дневной максимум '
prom_day_min = 'Дневной минимум '

valut_now = 'Текущий курс '
valut_day_max = 'Дневной максимум '
valut_day_min = 'Дневной минимум '

start_program = 'Program will started'

def check_Vatute():
    print('\n', start_program, '\n\n', start_collection, '\n')
    full_page = requests.get(Valute_Dollar, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("span", {"class": "arial_26 inlineblock pid-2186-last"})
    convert_min_dol = soup.findAll("span", {"class": "inlineblock pid-2186-low"})
    convert_max_dol = soup.findAll("span", {"class": "inlineblock pid-2186-high"})
    print(progress_bar + '1/2')
    time.sleep(2)

    full_page = requests.get(Valute_Euro, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_eu = soup.findAll("span", {"class": "arial_26 inlineblock pid-1691-last"})
    convert_min_eu = soup.findAll("span", {"class": "inlineblock pid-1691-low"})
    convert_max_eu = soup.findAll("span", {"class": "inlineblock pid-1691-high"})
    print(progress_bar + '2/2')
    print()
    time.sleep(.5)

    time_flow = input('Текущее время (hh-mm): ')
    print(packing)
    data = [
            [valut_now, convert_usd[0].text],
            [valut_day_min, convert_min_dol[0].text],
            [valut_day_max, convert_max_dol[0].text],
            [" ", " "],
            [valut_now, convert_eu[0].text],
            [valut_day_min, convert_min_eu[0].text],
            [valut_day_max, convert_max_eu[0].text],
    ]

    today = date.today()
    time_now = datetime.datetime.time(datetime.datetime.now())
    directory = 'Currency/'
    direction = 'Currency_'
    new_data = pd.DataFrame(data).rename_axis(None, axis=1)
    file_name = str(directory) + str(direction) + str(today) + '-' + str(time_flow)
    file_directory = file_name + '.xlsx'
    new_data.style.hide_index()
    writer = pd.ExcelWriter(file_directory, engine='xlsxwriter')
    new_data.to_excel(writer, sheet_name=str(sheet_name) + str(today), index=False)

    workbook = writer.book
    worksheet = writer.sheets[str(sheet_name) + str(today)]

    format_list = workbook.add_format({'border': 0, 'num_format': 'hh:mm:ss', 'size': 14, 'align': 'center'})
    format_date = workbook.add_format({'align': 'center'})
    worksheet.write('A1', time_now, format_list)
    worksheet.write('B1', today, format_date)
    format = workbook.add_format({'align': 'left'})
    num_format = workbook.add_format({'num_format': '0'})

    worksheet.set_landscape()
    worksheet.set_column('A:A', 20, format)
    worksheet.set_column('B:B', 10, num_format)

    writer.save()
    print('Файл с названием ' + str(direction) + str(today) + '-' + str(time_flow) + ' сохранен')
    time.sleep(3)


def check_Crypto():
    print('\n', start_program, '\n\n', start_collection, '\n')
    full_page = requests.get(Valute_Bitcoin, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_bitcoin = soup.findAll("span", {"class": "arial_26 inlineblock pid-945629-last"})
    convert_min_bitcoin = soup.findAll("span", {"class": "inlineblock pid-945629-low"})
    convert_max_bitcoin = soup.findAll("span", {"class": "inlineblock pid-945629-high"})
    print(progress_bar + '1/1')
    print()
    time.sleep(.5)

    time_flow = input('Текущее время (hh-mm): ')
    print(packing)
    data = [
            [valut_now, convert_bitcoin[0].text],
            [valut_day_min, convert_min_bitcoin[0].text],
            [valut_day_max, convert_max_bitcoin[0].text]
    ]

    today = date.today()
    time_now = datetime.datetime.time(datetime.datetime.now())
    directory = 'Cryptocurrencies/'
    direction = 'Crypto '
    new_data = pd.DataFrame(data).rename_axis(None, axis=1)
    file_name = str(directory) + str(direction) + str(today) + '-' + str(time_flow)
    file_directory = file_name + '.xlsx'
    new_data.style.hide_index()
    writer = pd.ExcelWriter(file_directory, engine='xlsxwriter')
    new_data.to_excel(writer, sheet_name=str(sheet_name) + str(today), index=False)

    workbook = writer.book
    worksheet = writer.sheets[str(sheet_name) + str(today)]

    format_list = workbook.add_format({'border': 0, 'num_format': 'hh:mm:ss', 'size': 14, 'align': 'center'})
    format_date = workbook.add_format({'align': 'center'})
    worksheet.write('A1', time_now, format_list)
    worksheet.write('B1', today, format_date)
    format = workbook.add_format({'align': 'left'})

    worksheet.set_landscape()
    worksheet.set_column('A:A', 50, format)
    worksheet.set_column('B:B', 30, format)

    writer.save()
    print('Файл с названием ' + str(direction) + str(today) + '-' + str(time_flow) + ' сохранен')
    time.sleep(3)


def check_Auto():
    print('\n', start_program, '\n\n', start_collection, '\n')
    time.sleep(.6)
    print(progress_bar + '1/5')
    full_page = requests.get(Promotions_Tesla, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_tesla = soup.findAll("span", {"class": "arial_26 inlineblock pid-13994-last"})
    convert_min_tesla = soup.findAll("span", {"class": "inlineblock pid-13994-low"})
    convert_max_tesla = soup.findAll("span", {"class": "inlineblock pid-13994-high"})
    time.sleep(2)

    print(progress_bar + '2/5')
    full_page = requests.get(Promotions_Nissan, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_nissan = soup.findAll("span", {"class": "arial_26 inlineblock pid-44127-last"})
    convert_min_nissan = soup.findAll("span", {"class": "inlineblock pid-44127-low"})
    convert_max_nissan = soup.findAll("span", {"class": "inlineblock pid-44127-high"})
    time.sleep(2)

    print(progress_bar + '3/5')
    full_page = requests.get(Promotions_GM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_gm = soup.findAll("span", {"class": "arial_26 inlineblock pid-239-last"})
    convert_min_gm = soup.findAll("span", {"class": "inlineblock pid-239-low"})
    convert_max_gm = soup.findAll("span", {"class": "inlineblock pid-239-high"})
    time.sleep(.5)

    print(progress_bar + '4/5')
    full_page = requests.get(Promotions_Ford, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_ford = soup.findAll("span", {"class": "arial_26 inlineblock pid-255-last"})
    convert_min_ford = soup.findAll("span", {"class": "inlineblock pid-255-low"})
    convert_max_ford = soup.findAll("span", {"class": "inlineblock pid-255-high"})
    time.sleep(2)

    print(progress_bar + '5/5')
    full_page = requests.get(Promotions_Daimler, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_daimler = soup.findAll("span", {"class": "arial_26 inlineblock pid-355-last"})
    convert_min_daimler = soup.findAll("span", {"class": "inlineblock pid-355-low"})
    convert_max_daimler = soup.findAll("span", {"class": "inlineblock pid-355-high"})
    time.sleep(2)

    time_flow = input('Текущее время (hh-mm): ')
    print(packing)
    prom_now = "Текущая стоимость акций "
    prom_day_max = 'Дневной максимум '
    prom_day_min = 'Дневной минимум '
    data = [
        [prom_now + str("Tesla"), convert_tesla[0].text],
        [prom_day_min, convert_min_tesla[0].text],
        [prom_day_max, convert_max_tesla[0].text],
        [" ", " "],
        [prom_now + str("Nissan"), convert_nissan[0].text],
        [prom_day_min, convert_min_nissan[0].text],
        [prom_day_max, convert_max_nissan[0].text],
        [" ", " "],
        [prom_now + str("General Motors"), convert_gm[0].text],
        [prom_day_min, convert_min_gm[0].text],
        [prom_day_max, convert_max_gm[0].text],
        [" ", " "],
        [prom_now + str("Ford"), convert_ford[0].text],
        [prom_day_min, convert_min_ford[0].text],
        [prom_day_max, convert_max_ford[0].text],
        [" ", " "],
        [prom_now + str("Daimler"), convert_daimler[0].text],
        [prom_day_min, convert_min_daimler[0].text],
        [prom_day_max, convert_max_daimler[0].text],
    ]

    today = date.today()
    directory = 'Carmakers/'
    direction = 'Сarmakers_'
    time_now = datetime.datetime.time(datetime.datetime.now())
    new_data = pd.DataFrame(data).rename_axis(None, axis=1)
    file_name = str(directory) + str(direction) + str(today) + '-' + str(time_flow)
    file_directory = file_name + '.xlsx'
    new_data.style.hide_index()
    writer = pd.ExcelWriter(file_directory, engine='xlsxwriter')
    new_data.to_excel(writer, sheet_name=str(sheet_name) + str(today), index=False)

    workbook = writer.book
    worksheet = writer.sheets[str(sheet_name) + str(today)]

    format_list = workbook.add_format({'border': 0, 'num_format': 'hh:mm:ss', 'size': 14, 'align': 'center'})
    format_date = workbook.add_format({'align': 'center'})
    worksheet.write('A1', time_now, format_list)
    worksheet.write('B1', today, format_date)
    format = workbook.add_format({'align': 'left'})

    worksheet.set_landscape()
    worksheet.set_column('A:A', 40, format)
    worksheet.set_column('B:B', 20, format)

    writer.save()
    print('Файл с названием ' + str(direction) + str(today) + '-' + str(time_flow) + ' сохранен')
    time.sleep(3)


def check_IT():
    print('\n', start_program, '\n\n', start_collection, '\n')
    full_page = requests.get(Promotions_AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_amd = soup.findAll("span", {"class": "arial_26 inlineblock pid-8274-last"})
    convert_min_amd = soup.findAll("span", {"class": "inlineblock pid-8274-low"})
    convert_max_amd = soup.findAll("span", {"class": "inlineblock pid-8274-high"})
    print(progress_bar + '1/8')
    time.sleep(2)

    full_page = requests.get(Promotions_Intel, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_intel = soup.findAll("span", {"class": "arial_26 inlineblock pid-251-last"})
    convert_min_intel = soup.findAll("span", {"class": "inlineblock pid-251-low"})
    convert_max_intel = soup.findAll("span", {"class": "inlineblock pid-251-high"})
    print(progress_bar + '2/8')
    time.sleep(2)

    full_page = requests.get(Promotions_Apple, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_apple = soup.findAll("span", {"class": "arial_26 inlineblock pid-6408-last"})
    convert_min_apple = soup.findAll("span", {"class": "inlineblock pid-6408-low"})
    convert_max_apple = soup.findAll("span", {"class": "inlineblock pid-6408-high"})
    print(progress_bar + '3/8')
    time.sleep(2)

    full_page = requests.get(Promotions_IBM, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_ibm = soup.findAll("span", {"class": "arial_26 inlineblock pid-8082-last"})
    convert_min_ibm = soup.findAll("span", {"class": "inlineblock pid-8082-low"})
    convert_max_ibm = soup.findAll("span", {"class": "inlineblock pid-8082-high"})
    print(progress_bar + '4/8')
    time.sleep(2)

    full_page = requests.get(Promotions_Microsoft, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_microsoft = soup.findAll("span", {"class": "arial_26 inlineblock pid-252-last"})
    convert_min_microsoft = soup.findAll("span", {"class": "inlineblock pid-252-low"})
    convert_max_microsoft = soup.findAll("span", {"class": "inlineblock pid-252-high"})
    print(progress_bar + '5/8')
    time.sleep(2)

    full_page = requests.get(Promotions_Google, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_google = soup.findAll("span", {"class": "arial_26 inlineblock pid-6369-last"})
    convert_min_google = soup.findAll("span", {"class": "inlineblock pid-6369-low"})
    convert_max_google = soup.findAll("span", {"class": "inlineblock pid-6369-high"})
    print(progress_bar + '6/8')
    time.sleep(2)

    full_page = requests.get(Promotions_Facebook, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_facebook = soup.findAll("span", {"class": "arial_26 inlineblock pid-26490-last"})
    convert_min_facebook = soup.findAll("span", {"class": "inlineblock pid-26490-low"})
    convert_max_facebook = soup.findAll("span", {"class": "inlineblock pid-26490-high"})
    print(progress_bar + '7/8')
    time.sleep(2)

    full_page = requests.get(Promotions_Yandex, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_yandex = soup.findAll("span", {"class": "arial_26 inlineblock pid-13999-last"})
    convert_min_yandex = soup.findAll("span", {"class": "inlineblock pid-13999-low"})
    convert_max_yandex = soup.findAll("span", {"class": "inlineblock pid-13999-high"})
    print(progress_bar + '8/8')
    time.sleep(.5)

    time_flow = input('Текущее время (hh-mm): ')
    print(packing)
    data = [
        [prom_now + str("AMD"), convert_amd[0].text],
        [prom_day_min, convert_min_amd[0].text],
        [prom_day_max, convert_max_amd[0].text],
        [" ", " "],
        [prom_now + str("Intel"), convert_intel[0].text],
        [prom_day_min, convert_min_intel[0].text],
        [prom_day_max, convert_max_intel[0].text],
        [" ", " "],
        [prom_now + str("Apple"), convert_apple[0].text],
        [prom_day_min, convert_min_apple[0].text],
        [prom_day_max, convert_max_apple[0].text],
        [" ", " "],
        [prom_now + str("IBM"), convert_ibm[0].text],
        [prom_day_min, convert_min_ibm[0].text],
        [prom_day_max, convert_max_ibm[0].text],
        [" ", " "],
        [prom_now + str("Microsoft"), convert_microsoft[0].text],
        [prom_day_min, convert_min_microsoft[0].text],
        [prom_day_max, convert_max_microsoft[0].text],
        [" ", " "],
        [prom_now + str("Google"), convert_google[0].text],
        [prom_day_min, convert_min_google[0].text],
        [prom_day_max, convert_max_google[0].text],
        [" ", " "],
        [prom_now + str("Facebook"), convert_facebook[0].text],
        [prom_day_min, convert_min_facebook[0].text],
        [prom_day_max, convert_max_facebook[0].text],
        [" ", " "],
        [prom_now + str("Yandex"), convert_yandex[0].text],
        [prom_day_min, convert_min_yandex[0].text],
        [prom_day_max, convert_max_yandex[0].text],
    ]

    today = date.today()
    time_now = datetime.datetime.time(datetime.datetime.now())
    directory = 'IT-corporations/'
    direction = 'IT_'
    new_data = pd.DataFrame(data).rename_axis(None, axis=1)
    file_name = str(directory) + str(direction) + str(today) + '-' + str(time_flow)
    file_directory = file_name + '.xlsx'
    new_data.style.hide_index()
    writer = pd.ExcelWriter(file_directory, engine='xlsxwriter')
    new_data.to_excel(writer, sheet_name=str(sheet_name) + str(today), index=False)

    workbook = writer.book
    worksheet = writer.sheets[str(sheet_name) + str(today)]

    format_list = workbook.add_format({'border': 0, 'num_format': 'hh:mm:ss', 'size': 14, 'align': 'center'})
    format_date = workbook.add_format({'align': 'center'})
    worksheet.write('A1', time_now, format_list)
    worksheet.write('B1', today, format_date)
    format = workbook.add_format({'align': 'left'})

    worksheet.set_landscape()
    worksheet.set_column('A:A', 40, format)
    worksheet.set_column('B:B', 20, format)

    writer.save()
    print('Файл с названием ' + str(direction) + str(today) + '-' + str(time_flow) + ' сохранен')
    time.sleep(3)


print('Change direction numeral: ')
change_Prom = input('1 - Currency, 2 - Cryptocurrencies, 3 -  Сarmakers, 4 - IT-corporations: ')

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