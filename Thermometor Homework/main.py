import tkinter as tk


window = tk.Tk()
window.title("Thermometer")
window.geometry("800x600")

thermo_label = tk.Label(window,text="Celsius->Fahrenheit",font=("Ariel",18,"bold"))
thermo_label.place(x=300,y=25)

temp_entry_label = tk.Label(window,text= "Enter Temperature in Celsius :")
temp_entry_label.place(x=300,y=75)

temp_entry = tk.Entry(window)
temp_entry.place(x=461,y=75)

temp_label_result = tk.Label(window,text="Temperuter in Fahrenheit")
temp_label_result.place



window.mainloop()   