import os

def get_words(filename):
    with open(filename,encoding='utf8') as f:
        text = f.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def get_words_dict(words):
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def main():
    filename = input('Введите путь к файлу')
    if not os.path.exists(filename):
        print('Указанный файл не существует')
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])

if __name__ == "__main__":
    main()