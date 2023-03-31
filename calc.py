import tkinter as tk


def calculate():
    number1 = float(entry_number1.get())
    number2 = float(entry_number2.get())
    option = int(option_var.get())

    if option == 1:
        result = number1 + number2
    elif option == 2:
        result = number1 - number2
    elif option == 3:
        result = number1 * number2
    elif option == 4:
        if number2 == 0:
            result = 'Cannot divide by zero'
        else:
            result = number1 / number2
    else:
        result = ''

    # Formata o resultado com duas casas decimais
    if isinstance(result, float):
        result = round(result, 2)

    label_result.config(text=f'Result: {result}')


def clear():
    entry_number1.delete(0, tk.END)
    entry_number2.delete(0, tk.END)
    option_var.set(1)
    label_result.config(text='Result: ')


root = tk.Tk()
root.title('Calculator')

# criação dos widgets
label_number1 = tk.Label(root, text='Enter a number:')
entry_number1 = tk.Entry(root)
label_number2 = tk.Label(root, text='Enter another number:')
entry_number2 = tk.Entry(root)
label_option = tk.Label(root, text='Choose an option:')
option_var = tk.IntVar()
option_var.set(1)
radio_add = tk.Radiobutton(root, text='+', variable=option_var, value=1)
radio_subtract = tk.Radiobutton(root, text='-', variable=option_var, value=2)
radio_multiply = tk.Radiobutton(root, text='*', variable=option_var, value=3)
radio_divide = tk.Radiobutton(root, text='/', variable=option_var, value=4)
button_calculate = tk.Button(root, text='Calculate', command=calculate)
button_clear = tk.Button(root, text='Clear', command=clear)
label_result = tk.Label(root, text='Result: ')

# layout dos widgets na janela
label_number1.grid(row=0, column=0)
entry_number1.grid(row=0, column=1)
label_number2.grid(row=1, column=0)
entry_number2.grid(row=1, column=1)
label_option.grid(row=2, column=0)
radio_add.grid(row=2, column=1, sticky='w')
radio_subtract.grid(row=3, column=1, sticky='w')
radio_multiply.grid(row=4, column=1, sticky='w')
radio_divide.grid(row=5, column=1, sticky='w')
button_calculate.grid(row=6, column=0)
button_clear.grid(row=6, column=1)
label_result.grid(row=7, column=0, columnspan=2)

root.mainloop()
