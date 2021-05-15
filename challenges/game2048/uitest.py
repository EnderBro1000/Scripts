from tkinter import *
import sys
 
def display():
    print(my_entry.get())
    # print(my_entry.get())
    my_label['text'] = my_entry.get()
    # my_label.set(root, my_entry.get())
    # my_label.pack(pady = 10)
 
def quit_window():
    root.destroy()
    sys.exit()
 
root = Tk()
root.geometry('300x300')
 
# results = StringVar()
# label = 
# my_label = Label(root, text = "Tkinter GUI Application")
my_label = Label(root, text = "Unset text")
# my_label['text'] = "ashgagegregtrg"
# my_label(text = "aaaashasghg")
my_label.pack(pady = 10)
 
my_entry = Entry(root)
my_entry.pack(pady = 30)

my_button = Button(root, text = "Print", command = display, width = 10)
my_button.pack(pady = 10)   

my_button2 = Button(root, text = "Quit", command = quit_window, width = 10)
my_button2.pack(pady = 10)

root.mainloop()