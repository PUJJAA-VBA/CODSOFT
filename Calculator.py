# CALCULATOR TASK

import tkinter  as tk
from tkinter import messagebox
import tkinter.font as tkFont
current_input = ""
result = ""
def on_button_click(button):
    global current_input
    if button == '=':
        try:
            result = eval(current_input)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            current_input = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            current_input = ""
    else:
        current_input += button
        display.insert(tk.END, button)
window = tk.Tk()
window.title("Calculator Task")
window.geometry("400x600")
display = tk.Entry(window, font=('Calibri', 24), justify='right')
display.pack(fill='x', padx=10, pady=10, ipadx=10, ipady=10)
button_frame = tk.Frame(window)
button_frame.pack()
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row, col = 1, 0
for button in buttons:
    tk.Button(button_frame, text=button, font=('Calibri', 18), width=5, height=2,
              command=lambda b=button: on_button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
window.mainloop()
