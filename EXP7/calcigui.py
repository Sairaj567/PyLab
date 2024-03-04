import tkinter as tk


def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.geometry("300x450")
root.title("Calculator")

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

list_of_numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
i = 0
for number in list_of_numbers:
    button = tk.Button(button_frame, width=4, height=1, text=number, font='lucida 20 bold')
    button.grid(row=int(i / 3), column=i % 3, padx=10, pady=5)
    i += 1
    button.bind("<Button-1>", calculate)


button_dot = tk.Button(button_frame, width=4, height=1, text=".", font='lucida 20 bold')
button_dot.grid(row=3, column=1)

button_equal = tk.Button(button_frame, width=4, height=1, text="=", font='lucida 20 bold')
button_equal.grid(row=3, column=2)

button_clear = tk.Button(button_frame, width=4, height=1, text="C", font='lucida 20 bold')
button_clear.grid(row=4, column=0)

button_divide = tk.Button(button_frame, width=4, height=1, text="/", font='lucida 20 bold')
button_divide.grid(row=4, column=1)

button_multiply = tk.Button(button_frame, width=4, height=1, text="*", font='lucida 20 bold')
button_multiply.grid(row=4, column=2)

button_subtract = tk.Button(button_frame, width=4, height=1, text="-", font='lucida 20 bold')
button_subtract.grid(row=5, column=0, pady=5)

button_add = tk.Button(button_frame, width=4, height=1, text="+", font='lucida 20 bold')
button_add.grid(row=5, column=1, pady=5)

button_dot.bind("<Button-1>", calculate)
button_equal.bind("<Button-1>", calculate)
button_clear.bind("<Button-1>", calculate)
button_divide.bind("<Button-1>", calculate)
button_multiply.bind("<Button-1>", calculate)
button_subtract.bind("<Button-1>", calculate)
button_add.bind("<Button-1>", calculate)

root.mainloop()
