import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import cdmatou as cdma

win = tk.Tk()
def make_menu(w):
    global the_menu
    the_menu = tk.Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

def Start ():    
    make_menu(win)
    win.title("CDMA Simulator")
    # drop down menu
    ttk.Label(win, text="Choisissez le nombre d'utilisateur:").grid(column=0, row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win, width=12, textvariable=number)
    numberChosen['values'] = (1, 2)
    numberChosen.grid(column=0, row=1)
    numberChosen.current(1)
    # checkbutton 2 (unchecked)
    chVarUn = tk.IntVar()
    bruit_checkbox = tk.Checkbutton(win, text="Bruit", onvalue = 1, offvalue = 0, variable=chVarUn)
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
        # button
    action = ttk.Button(win, text="Start", command= lambda: Start_simulation(numberChosen.get(), chVarUn.get(), msg_1.get('1.0', 'end-1c'), msg_2.get('1.0', 'end-1c')))
    action.grid(column=2, row=7)
    
    

def Start_simulation(nombre_users, bruit, msg_1, msg_2):
    # action.configure(text='Start')
    print('=========== Start simulation ===========')
    print('Nombre d utilisateurs: '+nombre_users)
    nois = 'Oui' if bruit == 1 else 'Non'
    print('Bruit: '+str(nois))

    print('Message 1: '+msg_1)
    print('Message 2: '+msg_2)
    #Cas 1 user
    if nombre_users =='1':
        print(cdma.text_to_bits(msg_1))
        Encoded_Volt = cdma.User_sending(msg_1,cdma.Key_1)
        if (bruit == 1):
            Traffic = cdma.Multiplexing_2 (Encoded_Volt ,cdma.Noise_Generator(len(Encoded_Volt)))
        else : Traffic = Encoded_Volt
    #Cas 2 users
    elif (nombre_users == '2'): 
        Encoded_Volt_1 = cdma.User_sending(msg_1,cdma.Key_1)
        Encoded_Volt_2 = cdma.User_sending(msg_2,cdma.Key_2 )
        diff =len(Encoded_Volt_1) - len(Encoded_Volt_2)
        if (bruit == 1):
            Traffic = cdma.Multiplexing(Encoded_Volt_1,Encoded_Volt_2,cdma.Noise_Generator(max(len(Encoded_Volt_1),len(Encoded_Volt_2))))
        else : Traffic = cdma.Multiplexing_2(Encoded_Volt_1,Encoded_Volt_2)
  

    #reception
    if nombre_users== '1':
        Reception=cdma.Decoder_1(Traffic,cdma.Key_1)
        print(Reception)
        #Back to Text 
        print (cdma.Back_to_text(Reception))

    elif nombre_users== '2':
        Reception_1,Reception_2=cdma.Decoder_2(Traffic,diff)
        print("Reception 1")
        print(Reception_1)
        print("Reception 2")
        print(Reception_2)
        #Back to text 
  
   




if __name__ == '__main__':
    Start() 
    win.mainloop()