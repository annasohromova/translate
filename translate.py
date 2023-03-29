import tkinter as tk

sona_translate = {}
translate_sona = {}

def failist_to_dict(f: str):
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')
        sona_translate[k] = v
        translate_sona[v] = k
    file.close()
    return sona_translate, translate_sona


# Словарь соответствия английских слов их переводам
def trn():
    if entry.get()==sona_translate.get():






# Функция для перевода слова
def translate(word):
    return sona_translate.get(word, word)

# Функция для обработки события нажатия кнопки
def translate_word():
    word = entry.get()
    translation = translate(word)
    label.config(text=translation)




def ds():
    a=failist_to_dict('sonad.txt')
    print(a)



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
