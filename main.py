# MyProfile app for entrepreneurs

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
postcode = ''
address = ''
info = ''
# business profile
ogrnip = 0
inn = 0
account = 0
bank = ''
bic = 0
cor_account = 0

print('Приложение MyProfile для предпринимателей')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while True:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in user_phone:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch
                email = input('Введите адрес электронной почты: ')

                user_postcode = input('Введите почтовый индекс: ')
                postcode = ''
                for ch in user_postcode:
                    if '0' <= ch <= '9':
                        postcode += ch
                address = input('Введите почтовый адрес (без индекса): ')

                info = input('Введите дополнительную информацию:\n')
            elif option2 == 2:
                # input business info
                while True:
                    # validate ogrnip
                    ogrnip = int(input('Введите ОГРНИП: '))
                    if 10 ** 14 <= ogrnip < 10 ** 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр')
                inn = int(input('Введите ИНН: '))
                while True:
                    # validate account number
                    account = int(input('Введите расчетный счет: '))
                    if 10 ** 19 <= account < 10 ** 20:
                        break
                    print('Расчетный счет должен содержать 20 цифр')
                bank = input('Введите название банка: ')
                bic = int(input('Введите БИК: '))
                cor_account = int(input('Введите корреспондентский счет: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # print general information
                print(SEPARATOR)
                print('Имя:    ', name)
                if 11 <= age % 100 <= 19:
                    years_name = 'лет'
                elif age % 10 == 1:
                    years_name = 'год'
                elif 2 <= age % 10 <= 4:
                    years_name = 'года'
                else:
                    years_name = 'лет'
                print('Возраст:', age, years_name)
                print('Телефон:', phone)
                print('E-mail: ', email)
                print('Индекс:', postcode)
                print('Адрес: ', address)

                if info:
                    print('')
                    print('Дополнительная информация:')
                    print(info)
            elif option2 == 2:
                # print full information
                print(SEPARATOR)
                print('Имя:    ', name)
                if 11 <= age % 100 <= 19:
                    years_name = 'лет'
                elif age % 10 == 1:
                    years_name = 'год'
                elif 2 <= age % 10 <= 4:
                    years_name = 'года'
                else:
                    years_name = 'лет'
                print('Возраст:', age, years_name)
                print('Телефон:', phone)
                print('E-mail: ', email)
                print('Индекс:', postcode)
                print('Адрес: ', address)

                if info:
                    print('')
                    print('Дополнительная информация:')
                    print(info)

                # print business info2
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП: ', ogrnip)
                print('ИНН:    ', inn)
                print('Банковские реквизиты')
                print('Р/с:    ', account)
                print('Банк:   ', bank)
                print('БИК:    ', bic)
                print('К/с:    ', cor_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
