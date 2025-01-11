from tkinter import *
from tkinter.messagebox import askyesno

window=Tk()

window.title("Products")
window.geometry('500x500')

def submit_address():
    n1 = n1_entry.get()
    n2 = n2_entry.get()
    n3 = n3_entry.get()
    n4 = n4_entry.get()
    n5 = n5_entry.get()

    addresst=n1+n2+n3+n4+n5
    result = askyesno("Confirm", f"Do you want to submit the address?\n\n{addresst}")
    
    if result: 
        textbox.insert(END, addresst)
    else:
        print("Address submission cancelled.")

Label(window, text="Address Window", font=("Arial", 16)).pack(pady=10)

Label(window, text="Street Name").pack(anchor=W, padx=10)
n1_entry = Entry(window, width=30)
n1_entry.pack(padx=10)

Label(window, text="Building Number").pack(anchor=W, padx=10)
n2_entry = Entry(window, width=30)
n2_entry.pack(padx=10)

Label(window, text="City").pack(anchor=W, padx=10)
n3_entry = Entry(window, width=30)
n3_entry.pack(padx=10)

Label(window, text="Region/State").pack(anchor=W, padx=10)
n4_entry = Entry(window, width=30)
n4_entry.pack(padx=10)

Label(window, text="Country").pack(anchor=W, padx=10)
n5_entry = Entry(window, width=30)
n5_entry.pack(padx=10)

textbox=Text(height=6)

submit_btn = Button(window, text="Submit", command=submit_address)
submit_btn.pack(pady=10)
textbox.pack()
window.mainloop()