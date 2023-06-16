# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле
from data_second import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас данные из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас данные из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def change_line(dataFile, numberRow, numberFile):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow]}?\nВведите ответ: ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: '))
        numberRow -= 1

    print(f"Меняем данную запись\n{dataFile[numberRow]}")
    if numberFile == 1:
        name = dataFile[numberRow].split('\n')[0]
        surname = dataFile[numberRow].split('\n')[1]
        phone = dataFile[numberRow].split('\n')[2]
        address = dataFile[numberRow].split('\n')[3]
    if numberFile == 2:
        name = dataFile[numberRow].split(';')[0]
        surname = dataFile[numberRow].split(';')[1]
        phone = dataFile[numberRow].split(';')[2]
        address = dataFile[numberRow].split(';')[3]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Имя\n"
                       f"2. Фамилия\n"
                       f"3. Номер телефона\n"
                       f"4. Адрес\n"
                       f"Введите ответ: "))
    while answer < 1 or answer > 4:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 4")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Имя\n"
                           f"2. Фамилия\n"
                           f"3. Номер телефона\n"
                           f"4. Адрес\n"
                           f"Введите ответ: "))
    if answer == 1:
        name = name_data()
    elif answer == 2:
        surname = surname_data()
    elif answer == 3:
        phone = phone_data()
    elif answer == 4:
        address = address_data()

    if numberFile == 1:
        data_first = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}'] + \
                     dataFile[numberRow + 1:]
        if numberRow + 1 == len(dataFile):
            data_first = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}\n']
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        data_second = dataFile[:numberRow] + [f'{name};{surname};{phone};{address}'] + \
                      dataFile[numberRow + 1:]
        if numberRow + 1 == len(dataFile):
            data_second = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                         dataFile[numberRow + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        change_line(data_first, number_journal, 1)
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        change_line(data_second, number_journal, 2)


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        # print(data_first[:number_journal - 1], data_first[number_journal + 1:]) error
        data_first = data_first[:number_journal - 1] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные