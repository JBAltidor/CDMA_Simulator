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
ttk.Label(win, text="Message 1:").grid(column=0, row=3)
msg_1 = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
msg_1.grid(column=0, row=4, sticky='WE', columnspan=3)

# scrolled text
ttk.Label(win, text="Message 2:").grid(column=0, row=5)
msg_2 = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
msg_2.grid(column=0, row=6, sticky='WE', columnspan=3)
if(numberChosen.get() == 1):
    msg_2.configure(state="disabled")


# button click event + name.get()
def Start_simulation(nombre_users, bruit, msg_1, msg_2):
    action.configure(text='Start')
    print('=========== Start simulation ===========')
    print('---------Number of users: '+nombre_users+' ---------')
    print('---------Noise: '+str(bruit)+' ---------')
    print('---------Message: '+msg_1+' ---------')
    print('---------Message: '+msg_2+' ---------')

# button
action = ttk.Button(win, text="Start", command= lambda: Start_simulation(numberChosen.get(), chVarUn.get(), msg_1.get('1.0', 'end-1c'), msg_2.get('1.0', 'end-1c')))
action.grid(column=2, row=7)
# action.configure(state='disabled')

win.mainloop()