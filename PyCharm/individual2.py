import random
def generate_password(word_file_path):
    try:
        with open(word_file_path, 'r') as file:
            words = [line.strip() for line in file if len(line.strip()) >= 3]

            if len(words) < 2:
                print("Недостаточно слов в файле.")
                return

            word1 = random.choice(words)
            word2 = random.choice(words)

            # Проверка на минимальную длину пароля
            while len(word1) + len(word2) < 8:
                word1 = random.choice(words)
                word2 = random.choice(words)

            # Проверка на максимальную длину пароля
            if len(word1) + len(word2) > 10:
                word2 = word2[:10 - len(word1)]

            # Создание пароля
            password = word1.capitalize() + word2.capitalize()

            print("Сгенерированный пароль:", password)

    except FileNotFoundError:
        print(f"Файл '{word_file_path}' не найден.")
word_file_path = 'wordlist.txt'
generate_password(word_file_path)
