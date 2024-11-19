import os
import csv


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
                print('----------')
                print('User  already exists')
                print('----------')
                return  
        
        # Если пользователь не найден, добавляем его
        writer = csv.DictWriter(f, fieldnames=columns)
        if f.tell() == 0:  # Проверяем, пуст ли файл
            writer.writeheader()
        
        writer.writerow({'name': name, 'password': password})
        print('----------')
        print('User  added successfully')
        print('----------')
        


def read():
    with open(FILENAME, 'r', newline='') as f:
        print('----------')
        myPass = input('Write your name for password: ')
        print('----------')
        reader = csv.DictReader(f)
        user_found = False  
        for row in reader: 
            if myPass == row['name']:  # Найден пользователь и выведены данные
                print('----------')
                print(f'Name: {myPass} and Password: {row["password"]}')  
                print('----------')
                user_found = True 
                break  
        if not user_found: #Не существует пользователя
            print('----------')
            print('User  not found')  
            print('----------')
        


def main():
    while True:
        print('----------')
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