# Import tkinter for the calculator window
from tkinter import *

# Import math for scientific calculations
import math


# Store the first number and selected operator
first_number = None
operator = None


# Add a number or decimal point to the display
def get_digit(value):
    current = result_label['text']
    result_label.config(text=current + str(value))


# Clear everything
def clear():
    global first_number, operator
    first_number = None
    operator = None
    result_label.config(text='')


# Store the first number and operator
def get_operator(op):
    global first_number, operator

    try:
        first_number = float(result_label['text'])
        operator = op
        result_label.config(text='')
    except ValueError:
        result_label.config(text='Error')


# Calculate the answer
def get_result():
    global first_number, operator

    try:
        second_number = float(result_label['text'])

        if operator == '+':
            answer = first_number + second_number

        elif operator == '-':
            answer = first_number - second_number

        elif operator == '*':
            answer = first_number * second_number

        elif operator == '/':
            if second_number == 0:
                result_label.config(text='Error')
                return
            answer = first_number / second_number

        elif operator == '^':
            answer = first_number ** second_number

        else:
            return

        result_label.config(text=format_number(answer))
        first_number = None
        operator = None

    except (ValueError, OverflowError):
        result_label.config(text='Error')


# Remove unnecessary .0 from whole numbers
def format_number(number):
    if number == int(number):
        return str(int(number))
    return str(round(number, 10))


# Calculate square root
def square_root():
    try:
        number = float(result_label['text'])
        if number < 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=format_number(math.sqrt(number)))
    except ValueError:
        result_label.config(text='Error')


# Calculate square
def square():
    try:
        number = float(result_label['text'])
        result_label.config(text=format_number(number ** 2))
    except ValueError:
        result_label.config(text='Error')


# Calculate percentage
def percentage():
    try:
        number = float(result_label['text'])
        result_label.config(text=format_number(number / 100))
    except ValueError:
        result_label.config(text='Error')


# Calculate reciprocal: 1/x
def reciprocal():
    try:
        number = float(result_label['text'])
        if number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=format_number(1 / number))
    except ValueError:
        result_label.config(text='Error')


# Calculate sin
def sine():
    try:
        number = float(result_label['text'])
        result_label.config(text=format_number(math.sin(math.radians(number))))
    except ValueError:
        result_label.config(text='Error')


# Calculate cos
def cosine():
    try:
        number = float(result_label['text'])
        result_label.config(text=format_number(math.cos(math.radians(number))))
    except ValueError:
        result_label.config(text='Error')


# Calculate tan
def tangent():
    try:
        number = float(result_label['text'])
        result_label.config(text=format_number(math.tan(math.radians(number))))
    except ValueError:
        result_label.config(text='Error')


# Calculate logarithm base 10
def logarithm():
    try:
        number = float(result_label['text'])
        if number <= 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=format_number(math.log10(number)))
    except ValueError:
        result_label.config(text='Error')


# Calculate natural logarithm
def natural_log():
    try:
        number = float(result_label['text'])
        if number <= 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=format_number(math.log(number)))
    except ValueError:
        result_label.config(text='Error')


# Add pi to the display
def pi():
    get_digit(math.pi)


# Add Euler's number to the display
def euler():
    get_digit(math.e)


# Change the sign of a number
def change_sign():
    try:
        number = float(result_label['text'])
        result_label.config(text=format_number(-number))
    except ValueError:
        result_label.config(text='Error')


# Create the main calculator window
root = Tk()
root.title('Scientific Calculator')
root.geometry('430x600')
root.resizable(0, 0)
root.configure(background='black')


# Calculator display
result_label = Label(
    root,
    text='',
    bg='black',
    fg='white',
    width=18,
    anchor='e'
)
result_label.grid(
    row=0,
    column=0,
    columnspan=6,
    padx=10,
    pady=(25, 20)
)
result_label.config(font=('verdana', 24, 'bold'))


# Common button settings
button_color = '#4D9BA8'
font_style = ('verdana', 11)


# Create a calculator button (can span several rows/columns)
def create_button(text, row, column, command, colspan=1, rowspan=1, color=None):
    button = Button(
        root,
        text=text,
        bg=color or button_color,
        fg='white',
        width=6,
        height=2,
        command=command
    )
    button.grid(
        row=row,
        column=column,
        columnspan=colspan,
        rowspan=rowspan,
        padx=3,
        pady=3,
        sticky='nsew'
    )
    button.config(font=font_style)


# Make all columns the same size
for i in range(6):
    root.grid_columnconfigure(i, weight=1, uniform='col')


# Extra colors for a more real-calculator look
operator_color = "#D69651"
clear_color = "#E42E1A"
equal_color = "#43B976"


# Row 1-2: scientific functions
create_button('sin', 1, 0, sine)
create_button('cos', 1, 1, cosine)
create_button('tan', 1, 2, tangent)
create_button('log', 1, 3, logarithm)
create_button('ln', 1, 4, natural_log)
create_button('√', 1, 5, square_root)

create_button('x²', 2, 0, square)
create_button('xʸ', 2, 1, lambda: get_operator('^'))
create_button('1/x', 2, 2, reciprocal)
create_button('π', 2, 3, pi)
create_button('e', 2, 4, euler)
create_button('%', 2, 5, percentage)


# Rows 3-6: number pad (left) with operators in column 3
create_button('7', 3, 0, lambda: get_digit(7))
create_button('8', 3, 1, lambda: get_digit(8))
create_button('9', 3, 2, lambda: get_digit(9))
create_button('÷', 3, 3, lambda: get_operator('/'), color=operator_color)

create_button('4', 4, 0, lambda: get_digit(4))
create_button('5', 4, 1, lambda: get_digit(5))
create_button('6', 4, 2, lambda: get_digit(6))
create_button('×', 4, 3, lambda: get_operator('*'), color=operator_color)

create_button('1', 5, 0, lambda: get_digit(1))
create_button('2', 5, 1, lambda: get_digit(2))
create_button('3', 5, 2, lambda: get_digit(3))
create_button('−', 5, 3, lambda: get_operator('-'), color=operator_color)

create_button('0', 6, 0, lambda: get_digit(0), colspan=2)
create_button('.', 6, 2, lambda: get_digit('.'))
create_button('+', 6, 3, lambda: get_operator('+'), color=operator_color)


# Right side: brackets, clear, sign and big equals button
create_button('(', 3, 4, lambda: get_digit('('))
create_button(')', 3, 5, lambda: get_digit(')'))
create_button('C', 4, 4, clear, color=clear_color)
create_button('±', 4, 5, change_sign)
create_button('=', 5, 4, get_result, colspan=2, rowspan=2, color=equal_color)


# Keep the calculator window open
root.mainloop()
