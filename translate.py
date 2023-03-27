import tkinter as tk

# Словарь соответствия английских слов их переводам
translation_dict = {
    'hello': 'привет',
    'world': 'мир',
    'python': 'питон'
}

# Функция для перевода слова
def translate(word):
    return translation_dict.get(word, word)

# Функция для обработки события нажатия кнопки
def translate_word():
    word = entry.get()
    translation = translate(word)
    label.config(text=translation)

# Создаем графический интерфейс
root = tk.Tk()
root.title('Переводчик')

# Создаем текстовое поле и кнопку
entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)
button = tk.Button(root, text='Перевести', command=translate_word)
button.pack(padx=10, pady=10)

# Создаем метку для вывода перевода
label = tk.Label(root, text='')
label.pack(padx=10, pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()