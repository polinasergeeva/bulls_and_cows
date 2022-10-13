from tkinter import *
from tkinter import messagebox, Label
import random


def on_closing():
    """
    Функция для подтверждения выхода из приложения (messagebox)
    """

    if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
        window.destroy()


def is_valid(new_value: str) -> bool:
    """
    Функция, которая проверяет введенное пользователем число на корректность:
    - должны быть введены только цифры
    - должно быть введено ровно 4 цифры
    - цифры не должны повторяться
    """
    if not new_value.isdigit() or len(new_value) != 4 or len(set(new_value)) != 4:
        return False

    return True


def create_computer_number_zerofirst() -> str:
    """
    Функция, которая генерирует загаданное компьютером число
    """

    comp_number = str(random.randint(1000, 9999))

    digits = set(comp_number)
    count_digits = len(digits)

    while count_digits != 4:
        if count_digits == 3:
            comp_number = '0'
            for d in list(digits):
                comp_number += d
        else:
            comp_number = str(random.randint(1000, 9999))

        digits = set(comp_number)
        count_digits = len(digits)

    return comp_number


def print_bulls_cows() -> None:
    """ Функция, которая сравнивает число, введенное пользователем, с числом, загаданным компьютером,
    и выводит на экран количество 'быков' - цифр, стоящих на своих местах, и количество 'коров' - цифр,
    которые есть в загаданном числе, но стоящих на других местах."""

    global computer_number
    count_cows = 0
    count_bulls = 0

    user_number = entry.get()

    if not is_valid(user_number):
        messagebox.showerror(message='Вы ввели некорректное число, повторите попытку.')
        return
    if user_number == computer_number:
        messagebox.showinfo(message='Вы победили')
        entry.delete(0, END)
        label_cow_bull.config(text='')
        return

    for pos in range(4):
        user_digit = user_number[pos]
        computer_digit = computer_number[pos]

        if user_digit in computer_number:
            count_cows += 1

        if user_digit == computer_digit:
            count_bulls += 1  # count_bulls = count_bulls + 1

    count_cows -= count_bulls
    
    prev = label_cow_bull['text']
    text_label = prev + '\n' + 'Количество коров: ' + str(count_cows) + ' | Количество быков: ' + str(count_bulls)
    label_cow_bull.config(text=text_label)


def add_buttonlabel():
    """ Функция, запускается при нажатии кнопки 'Начать игру'. Создает поле для ввода числа пользователем, кнопку 'OK',
    надпись 'Введите выше число:'. А также запускает функцию, которая создает число, загаданное компьютером. """
    
    global computer_number

    computer_number = create_computer_number_zerofirst()

    label = Label(window, text='Введите ваше число:', font=('Arial Bold', 16), bg='light yellow')
    label.place(x=580, y=70)

    entry.place(x=800, y=76)
    btn1 = Button(window, height=1, width=2, text='OK', fg='white', bg='brown', command=print_bulls_cows)
    btn1.place(x=870, y=73)


computer_number = 0

window = Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.resizable(False, False)
window.title('Bulls and cows')
window.geometry('1000x550')
window.configure(background='red')

canvas = Canvas(window, width=1000, height=550, bg='light yellow')
canvas.pack()

our_image = PhotoImage(file="jj.png")
our_image = our_image.subsample(4, 4)
our_label = Label(window)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x=100, y=20)

btn = Button(window, height=5, width=30, text='Начать игру', fg='white', bg='brown', command=add_buttonlabel)
btn.place(relx=0.2, rely=0.78)

entry = Entry(window, width=10)

label_cow_bull = Label(window, text='', bg='light yellow')
label_cow_bull.place(x=580, y=100)

lbl = Label(window, text="Bulls and cows", font=("Arial Bold", 20), bg='light yellow')
lbl.place(x=215, y=382)

window.mainloop()
