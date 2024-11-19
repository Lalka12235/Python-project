FILENAME = 'test.txt'
def write():
    print('-----------')
    message = input('Введите строку: ')
    print('-----------')
    with open(FILENAME, 'r+') as f:
        f.write(message)

def read():
    with open(FILENAME, 'r') as f:
        print('-----------')
        print('Данные из файла: ')
        print(f.read())
        print('-----------')

def clear():
    with open(FILENAME, 'w+') as f:
        print(f.read())
        print('-----------')
        print('Файл Перезаписан')
        print('-----------')


while True:
    action = input('1)Запись строки в файл\n2)Чтение строки из файла\n3)Перезапись файла\n4)Выход\n')
    match action:
        case '1':
            write()
        case '2':
            read()
        case '3':
            clear()
        case '4':
            break
        case _:
            print('Некорректный ввод')
