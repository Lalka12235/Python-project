from bs4 import BeautifulSoup
import requests

URL = input('Введите ссылку на страницу с Википедии: ')
response = requests.get(URL)

# Проверка успешности запроса
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем блок с нужным классом
    block = soup.find('div', id='content')
    
    if block:
        # Основная информация с страницы
        title = block.find('h1', id='firstHeading')
        body = block.find_all('p')
        
        # Поиск ссылки на скачивание картинки
        img_div = block.find('div', id='mw-content-text')
        img = img_div.find('img') if img_div else None
        
        # Если изображение найдено, скачиваем его
        if img:
            img_url = img['src']
            img_url = 'https:' + img_url if img_url.startswith('//') else img_url
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()  # Проверяем успешность запроса
                with open('downloaded_image.jpg', 'wb') as f:
                    f.write(img_response.content)
                print('________________')
                print('Картинка скачана')
                print('________________')
            except requests.exceptions.RequestException as e:
                print(f'Ошибка скачивания картинки: {e}')
        else:
            print('Изображение не найдено.')
        
        if title and body:
            print('______________')
            print('Название страницы в Википедии: ', title.text)
            print('______________')
            print('Описание Статьи:')
            for paragraph in body:
                print(paragraph.text.strip(), end='\n')
                print('')

        else:
            print('Информация не найдена')

    else:
        print('Блок с указанным классом не найден.')
else:
    print(f'Ошибка запроса: {response.status_code}')
