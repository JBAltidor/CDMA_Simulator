import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import cdma as cdma
import signals as graph

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
    nois = 'Oui' if bruit == 1 else 'Non'
    print('---------Noise: '+str(nois)+' ---------')

    print('---------Message: '+msg_1+' ---------')
    print('---------Message: '+msg_2+' ---------')

    if (nombre_users == '1'):
        Key = cdma.Walsh()[2] 
        Encoded_Volt = cdma.User_sending(msg_1,Key)
        if (bruit == 1):
            Traffic = cdma.Multiplexing_2 (Encoded_Volt ,cdma.Noise_Generator(len(Encoded_Volt)))
        else : Traffic = Encoded_Volt
        print(Key)
        print(Traffic)
        print(cdma.User_receiving(Traffic,Key))
    elif (nombre_users == '2'):
        Key_1 = cdma.Walsh()[2] 
        Key_2 = cdma.Walsh()[3] 
        Encoded_Volt_1 = cdma.User_sending(msg_1,Key_1)
        Encoded_Volt_2 = cdma.User_sending(msg_2,Key_2)
        if (bruit == 1):
            m1,m2=cdma.padding(Encoded_Volt_1,Encoded_Volt_2)
            Traffic = cdma.Multiplexing(m1,m2,cdma.Noise_Generator(len(m1)))
        else : Traffic = cdma.Multiplexing_2(*cdma.padding(Encoded_Volt_1,Encoded_Volt_2))

        print(Key_1)
        print(Key_2)
        print(Traffic)
        print(cdma.User_receiving(Traffic,Key_1))
        print(cdma.User_receiving(Traffic,Key_2))


   


# button
action = ttk.Button(win, text="Start", command= lambda: Start_simulation(numberChosen.get(), chVarUn.get(), msg_1.get('1.0', 'end-1c'), msg_2.get('1.0', 'end-1c')))
action.grid(column=2, row=7)
# action.configure(state='disabled')

win.mainloop()



# Je trouve vraiment ca ridicule de mettre ces etapes, cuz 
# donnees yo trop incomprehensibles