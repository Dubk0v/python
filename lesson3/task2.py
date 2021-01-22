'''
2.Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
'''


def base(name, surname, date_of_birthday, live_city, email, phone_num):
    print(f'name: {name}, surname: {surname}, birthday: {date_of_birthday}, city: {live_city},'
          f'email: {email}, phone: {phone_num}')


base(name=1, surname=2, date_of_birthday=3, live_city=4, email=5, phone_num=6)
