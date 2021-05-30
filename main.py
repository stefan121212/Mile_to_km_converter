from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=30, pady=10)
def button_clicked():
    q = float(input.get())
    result = round(q * 1.60934, 1)
    my_label3.config(text=f"{result}")

input = Entry(width=10)
input.grid(column=1, row=0)

print(type(input))
my_label = Label(text="Miles", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=0)

my_label2 = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0", font=("Arial", 12, "bold"))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km", font=("Arial", 12, "bold"))
my_label4.grid(column=2, row=1)



my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)









window.mainloop()