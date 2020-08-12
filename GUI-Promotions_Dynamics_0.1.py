# Импортируем все из библиотеки TKinter
from tkinter import *

# Эта библиотека нужна для работы с отправкой URL запросов
import requests

# Создаем главный объект (по сути окно приложения)
root = Tk()


# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    # Получаем данные от пользователя
    city = cityField.get()

    # данные о погоде будем брать с сайта openweathermap.org
    # ниже пропишите свой API ключ, который получите в кабинете пользователя на сайте openweathermap.org
    key = '4b23f5e0255ec6fa3a6d0fb342e02eb5'
    # ссылка, с которой мы получим все данные в формате JSON
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    # Отправляем запрос по определенному URL
    result = requests.get(url, params=params)
    # Получаем JSON ответ по этому URL
    weather = result.json()

    # Полученные данные добавляем в текстовую надпись для отображения пользователю
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


# Настройки главного окна

# Указываем фоновый цвет
root['bg'] = '#fafafa'
root.title('Weather')
root.geometry('600x500')
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#ffb700', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

clear = Label(frame_top, text=' ', bg='#ffb700', font=40)
clear.pack()

btn = Button(frame_top, text='Вывести данные о погоде', width=30, bg='#FFF', height=1, font='Arial 16', command=get_weather)
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
info = Label(frame_bottom, text='Info', bg='#ffb700', font='Arial 18')
info.pack()

root.mainloop()