import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(input_entry.get())
        if temp_Val == 'Celsius':
            f = (temp * 9 / 5) + 32
            result_label.config(text=f"{f:.1f} Fahrenheit")
            messagebox.showinfo("Temperature Converter", "Successfully converted to Fahrenheit")
        elif temp_Val == 'Fahrenheit':
            c = (temp - 32) * 5 / 9
            result_label.config(text=f"{c:.1f} Celsius")
            messagebox.showinfo("Temperature Converter", "Successfully converted to Celsius")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid numeric value.")

root = tk.Tk()
root.title('Temperature Converter')

# Set window size and position
root.geometry('300x150+600+200')  # Width x Height + X + Y

temp_Val = "Celsius"  # Default temperature scale

input_label = tk.Label(root, text="Enter temperature")
input_entry = tk.Entry(root)
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)

result_label = tk.Label(root)
result_label.grid(row=1, column=0, columnspan=2)

dropDownList = ["Celsius", "Fahrenheit"]
var = tk.StringVar()
var.set(dropDownList[0])
drop_down = tk.OptionMenu(root, var, *dropDownList)
drop_down.grid(row=0, column=2)

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, columnspan=2)

root.mainloop()
