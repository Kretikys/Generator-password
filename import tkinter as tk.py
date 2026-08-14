import string  # Импортируем модуль string для доступа к наборам символов
import tkinter as tk  # Импортируем Tkinter для создания интерфейса
import pyperclip  # Импортируем модуль для буфера обмена (pip install pyperclip)
import secrets  # Импортируем модуль secrets для генерации криптографически безопасных паролей



# Переменная для отслеживания текущего цвета фона
current_bg_index = 0
bg_colors = ["#1c1026", "#09020e", "#2d1b3d", "#1a0f2e"]  # Набор цветов для переключения

def toggle_background():
    """Переключает фон между несколькими цветами"""
    global current_bg_index
    current_bg_index = (current_bg_index + 1) % len(bg_colors)
    root.config(bg=bg_colors[current_bg_index])



def generate_password():
    chars = string.ascii_letters  # Базовый набор: все латинские буквы
    if digits_var.get():
        chars += string.digits  # Добавляем цифры, если чекбокс активен
    if symbols_var.get():
        chars += string.punctuation  # Добавляем спецсимволы, если чекбокс активен
    length = length_slider.get()  # Получаем длину со слайдера
    password = ""
    for i in range(length):
        password += secrets.choice(chars)

    # Выводим пароль в поле для результата
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    """Копирует сгенерированный пароль в буфер обмена"""
    pwd = result_entry.get()
    if pwd:
        pyperclip.copy(pwd)
        copy_lbl.config(text=" Пароль скопирован в буфер!")

# ==================== НАСТРОЙКА ОКНА ====================
root = tk.Tk()
root.title("Генератор безопасных паролей")
root.geometry("400x380")
root.config(bg="#1c1026")  # Темный фон

# ==================== ВЕРХНЯЯ ПАНЕЛЬ (ЗАГОЛОВОК + КНОПКА) ====================
top_frame = tk.Frame(root, bg="#1c1026")
top_frame.pack(pady=10, fill=tk.X, padx=10)

# Заголовок слева
title_lbl = tk.Label(
    top_frame,
    text=" Генератор паролей",
    font=("Arial", 16, "bold"),
    bg="#1c1026",
    fg="#f472b6",  # Розовый цвет
)
title_lbl.pack(side=tk.LEFT)

# Кнопка смены фона справа
change_fon = tk.Button(top_frame, text="Сменить фон", command=toggle_background, bg="#f472b6", fg="#0f0514", font=("Arial", 10, "bold"))
change_fon.pack(side=tk.RIGHT)

# ==================== ЗАГОЛОВОК ====================

# ==================== СЛАЙДЕР ДЛИНЫ ====================
tk.Label(root, text="Длина пароля:", bg="#1c1026", fg="white").pack()

length_slider = tk.Scale(
    root,
    from_=6,  # Минимальная длина
    to=24,  # Максимальная длина
    orient=tk.HORIZONTAL,  # Горизонтальный слайдер
    bg="#1c1026",
    fg="white",
    highlightbackground="#1c1026",
)
length_slider.set(12)  # Значение по умолчанию - 12 символов
length_slider.pack(pady=5)

# ==================== ЧЕКБОКСЫ ====================
digits_var = tk.BooleanVar(value=True)  # По умолчанию включено
digits_chk = tk.Checkbutton(
    root,
    text="Использовать цифры (0-9)",
    variable=digits_var,
    bg="#1c1026",
    fg="#fdf2f8",  # Светлый текст
    selectcolor="#09020e",
)
digits_chk.pack(anchor="w", padx=80)

symbols_var = tk.BooleanVar(value=True)  # По умолчанию включено
symbols_chk = tk.Checkbutton(
    root,
    text="Использовать спецсимволы (!@#$)",
    variable=symbols_var,
    bg="#1c1026",
    fg="#fdf2f8",
    selectcolor="#09020e",
)
symbols_chk.pack(anchor="w", padx=80)

# ==================== КНОПКА ГЕНЕРАЦИИ ====================
gen_btn = tk.Button(
    root,
    text="Сгенерировать пароль",
    command=generate_password,
    bg="#f472b6",
    fg="#0f0514",
    font=("Arial", 10, "bold"),
)
gen_btn.pack(pady=10)

# ==================== ПОЛЕ ДЛЯ РЕЗУЛЬТАТА ====================
result_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=22)
result_entry.pack(pady=5)


# ==================== КНОПКА КОПИРОВАНИЯ ====================
copy_btn = tk.Button(
    root, text="Скопировать в буфер", command=copy_to_clipboard
)
copy_btn.pack(pady=5)

# ==================== СООБЩЕНИЕ О КОПИРОВАНИИ ====================
copy_lbl = tk.Label(
    root,
    text="",
    bg="#1c1026",
    fg="#4ade80",  # Зеленый для сообщения об успехе
)
copy_lbl.pack()

# ==================== ЗАПУСК ПРОГРАММЫ ====================
root.mainloop()