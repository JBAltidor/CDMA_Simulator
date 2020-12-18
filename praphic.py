import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
win = tk.Tk()
win.title("CDMA Simulator")
# win.resizable(0,0)


# drop down menu
ttk.Label(win, text="Select number of users:").grid(column=0, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2)
numberChosen.grid(column=0, row=1)
numberChosen.current(1)


# checkbutton 2 (unchecked)
chVarUn = tk.IntVar()
bruit_checkbox = tk.Checkbutton(win, text="Noise", onvalue = 1, offvalue = 0, variable=chVarUn)
bruit_checkbox.toggle()
bruit_checkbox.grid(column=0, row=2, sticky=tk.W, columnspan=3)


# scrolled text
ttk.Label(win, text="Message:").grid(column=0, row=3)
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=4, sticky='WE', columnspan=3)

# button click event + name.get()
def Start_simulation(nombre_users, bruit, msg):
    action.configure(text='Start')
    print('=========== Start simulation ===========')
    print('---------Number of users: '+nombre_users+' ---------')
    print('---------Noice: '+str(bruit)+' ---------')
    print('---------Message: '+msg+' ---------')

# button
action = ttk.Button(win, text="Start", command= lambda: Start_simulation(numberChosen.get(), chVarUn.get(), scr.get('1.0', 'end-1c')))
action.grid(column=2, row=5)
# action.configure(state='disabled')

win.mainloop()