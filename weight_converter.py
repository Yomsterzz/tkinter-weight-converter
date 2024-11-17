import tkinter as tk

def convert():
    kg = float(entry1.get())  
    gram_display.delete(1.0, tk.END) 
    gram_display.insert(tk.END, kg * 1000) 
    pound_display.delete(1.0, tk.END) 
    pound_display.insert(tk.END, kg * 2.20462) 
    ounce_display.delete(1.0, tk.END)
    ounce_display.insert(tk.END, kg * 35.274) 

window = tk.Tk()
window.title("Weight Converter")
window.geometry("800x400")
window.configure(bg="pale turquoise")

label1 = tk.Label(window, text="Enter weight in kilograms:", font=("Helvetica", 16), fg="red", bg="pale turquoise")
entry1 = tk.Entry(window, font=("Helvetica", 16))
button1 = tk.Button(window, text="Convert", font=("Helvetica", 16), command=convert)

gram = tk.Label(window, text="Gram", font=("Helvetica", 16), bg="pale turquoise")
pound = tk.Label(window, text="Pound", font=("Helvetica", 16), bg="pale turquoise")
ounce = tk.Label(window, text="Ounce", font=("Helvetica", 16), bg="pale turquoise")

gram_display = tk.Text(window, font=("Helvetica", 16), width=10, height=1)
pound_display = tk.Text(window, font=("Helvetica", 16), width=10, height=1)
ounce_display = tk.Text(window, font=("Helvetica", 16), width=10, height=1)

label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
button1.grid(row=0, column=2, padx=10, pady=10)

gram.grid(row=1, column=0, padx=10, pady=10)
pound.grid(row=1, column=1, padx=10, pady=10)
ounce.grid(row=1, column=2, padx=10, pady=10)

gram_display.grid(row=2, column=0, padx=10, pady=10)
pound_display.grid(row=2, column=1, padx=10, pady=10)
ounce_display.grid(row=2, column=2, padx=10, pady=10)

window.columnconfigure(1, weight=1)

window.mainloop()
