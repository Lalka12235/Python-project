import os

def check_path(path):
    if os.path.exists(path):
        print('Хорошо, можем начинать работу')
        return True
    else:
        print('Укажите верный путь')
        return False


def check_dir(path: str):
    temp = 'app' if path.endswith('app') else 'src'
    check_path(path)
    print(f'{temp}\\')
    if check_path:
        directory = os.listdir(path)
        for dir in directory:
            if dir != '__pycache__' and dir != '__init__.py' and dir != 'config.py':
                print(f'    {dir}\\')
                for files in os.listdir(f'{path}\\{dir}'):
                    if files != '__pycache__':
                        print(f'        {files}')

def main():
    path = input('Введите абсолютный путь к директории(app|| src): ')
    check_dir(path)


if __name__ == '__main__':
    main()