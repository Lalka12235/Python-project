import os
import csv
import bcrypt

FILENAME = 'test.txt'

def save():
    print('----------')
    name = input('Write your name: ')
    password = input('Write your password: ')
    print('----------')
    columns = ['name', 'password']

    with open(FILENAME, 'a+', newline='') as f:
        f.seek(0)
        reader = csv.DictReader(f, fieldnames=columns)

        # Проверяем существующих пользователей
        for row in reader:
            if row['name'] == name:
                print('User  already exists')
                print('----------')
                return  

        # Если пользователь не найден, добавляем его
        writer = csv.DictWriter(f, fieldnames=columns)
        if f.tell() == 0:  # Проверяем, пуст ли файл
            writer.writeheader()

        # Хешируем пароль перед сохранением
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        writer.writerow({'name': name, 'password': hashed_password.decode('utf-8')})
        print('User  added successfully')
        print('----------')


def read():
    with open(FILENAME, 'r', newline='') as f:
        myPass = input('Write your name for password: ')
        reader = csv.DictReader(f)
        user_found = False  
        for row in reader:
            if myPass == row['name']:  # Найден пользователь
                # Проверяем, соответствует ли введённый пароль хешу
                password_input = input('Write your password to verify: ')
                if bcrypt.checkpw(password_input.encode('utf-8'), row['password'].encode('utf-8')):
                    print(f'Name: {myPass} and Password: {row["password"]}')  
                    print('----------')
                else:
                    print('Password is incorrect')  
                    print('----------')
                user_found = True 
                break  
        if not user_found:  # Не существует пользователя
            print('User  not found')  
            print('----------')


def main():
    while True:
        action = input(f'1)Создать пароль и привязать к имени\n2)Прочитать свой пароль\n3)Выход\n')
        print('----------')
        if action == '1':
            save()
        elif action == '2':
            read()
        else:
            break


if __name__ == '__main__':
    main()