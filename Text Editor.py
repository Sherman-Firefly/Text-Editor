from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window=Tk()
window.title("Text Editor")
window.geometry("600x700")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def openfile():
    """Open file for editing"""
    filepath=askopenfilename(filetypes=[('Textfiles','.txt'),('All files','*.*')])
    if not filepath:
        return 
    txt_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Editor Window{filepath}")

def savefile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[('Textfiles','.txt'),('All files','*.*')])
    if not filepath:
        return
    with open(filepath,"r") as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Save Window{filepath}")

txt_edit=Text(window)
fr_button=Frame(window,relief=RAISED,bd=3)
btn_open=Button(fr_button,text="Open",command=openfile)
btn_save=Button(fr_button,text="Save as",command=savefile)

btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_button.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")

window.mainloop()