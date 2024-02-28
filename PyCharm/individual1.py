def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def process_text(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) > 1 and is_vowel(word[0]) and is_vowel(word[-1]):
                        print(word)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Создаем файл с текстом
example_text = """Hello world
Python programming is fun
OpenAI is awesome
Text processing in Python"""

with open('example.txt', 'w') as file:
    file.write(example_text)

process_text('example.txt')
