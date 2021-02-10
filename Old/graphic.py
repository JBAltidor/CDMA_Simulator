import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import cdma as cdma

#import signals as graph
#from Graphics import Tkinter

class StationeryFunctions:
    def __init__(self, text):
        self.text = text
        self.create_binding_keys()
        self.binding_functions_config()
        self.join_function_with_main_stream()


    def join_function_with_main_stream(self):
        self.text.storeobj['Copy']   =  self.copy
        self.text.storeobj['Cut']    =  self.cut
        self.text.storeobj['Paste']  =  self.paste
        self.text.storeobj['SelectAll']=self.select_all
        self.text.storeobj['DeselectAll']=self.deselect_all
        return

    def binding_functions_config(self):
        self.text.tag_configure("sel", background="skyblue")
        return

    def copy(self, event):
        self.text.event_generate("&lt;&lt;Copy>>")
        return

    def paste(self, event):
        self.text.event_generate("&lt;&lt;Paste>>")
        return

    def cut(self, event):
        self.text.event_generate("&lt;&lt;Cut>>")
        return

    def create_binding_keys(self):
        for key in ["&lt;Control-a>","&lt;Control-A>"]:
            self.text.master.bind(key, self.select_all)
        for key in ["&lt;Button-1>","&lt;Return>"]:
            self.text.master.bind(key, self.deselect_all)
        return

    def select_all(self, event):
        self.text.tag_add("sel",'1.0','end')
        return


    def deselect_all(self, event):
        self.text.tag_remove("sel",'1.0','end')
        return



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
    print('Nombre d utilisateurs: '+nombre_users)
    nois = 'Oui' if bruit == 1 else 'Non'
    print('Bruit: '+str(nois))

    print('Message 1: '+msg_1)
    print('Message 2: '+msg_2)

    if (nombre_users == '1'):
        Key = cdma.Walsh()[2] 
        Encoded_Volt = cdma.User_sending(msg_1,Key)
        if (bruit == 1):
            Traffic = cdma.Multiplexing_2 (Encoded_Volt ,cdma.Noise_Generator(len(Encoded_Volt)))
        else : Traffic = Encoded_Volt
        print("La cle de l'utilisateur est :",Key, "\n")
        print("\nTraffic transitant sur le canal \n",Traffic,'\n')
        print("Message a la reception : ",cdma.User_receiving(Traffic,Key))
        print ("\nLe Bit Error Rate est :",cdma.BER(cdma.binaire_to_ternaire(cdma.text_to_bits(msg_1)), cdma.Decoder(Traffic,Key)))
    elif (nombre_users == '2'):
        Key_1 = cdma.Walsh()[2] 
        Key_2 = cdma.Walsh()[3] 
        Encoded_Volt_1 = cdma.User_sending(msg_1,Key_1)
        Encoded_Volt_2 = cdma.User_sending(msg_2,Key_2)
        if (bruit == 1):
            m1,m2=cdma.padding(Encoded_Volt_1,Encoded_Volt_2)
            Traffic = cdma.Multiplexing(m1,m2,cdma.Noise_Generator(len(m1)))
        else : Traffic = cdma.Multiplexing_2(*cdma.padding(Encoded_Volt_1,Encoded_Volt_2))

        print("La cle de l'utilisateur 1 est :",Key_1)
        print("La cle de l'utilisateur 2 est :",Key_2)
        print("\nTraffic transitant sur le canal \n",Traffic,'\n')
        print("Message a la reception pour l'utilisateur 1 : ",cdma.User_receiving(Traffic,Key_1))
        print("Message a la reception pour l'utilisateur 2 : ",cdma.User_receiving(Traffic,Key_2))
        print ("\nLe Bit Error Rate pour l'utilisateur 1 est :",cdma.BER(cdma.binaire_to_ternaire(cdma.text_to_bits(msg_1)), cdma.Decoder(Traffic,Key_1)))
        print ("\nLe Bit Error Rate pour l'utilisateur 2 est :",cdma.BER(cdma.binaire_to_ternaire(cdma.text_to_bits(msg_2)), cdma.Decoder(Traffic,Key_2)))

   


# button
action = ttk.Button(win, text="Start", command= lambda: Start_simulation(numberChosen.get(), chVarUn.get(), msg_1.get('1.0', 'end-1c'), msg_2.get('1.0', 'end-1c')))
action.grid(column=2, row=7)
# action.configure(state='disabled')

win.mainloop()

# root = tk.Tk()
# pad = tk.Text(root,wrap='none')
# pad.storeobj = {}
# StationeryFunctions(pad)
# pad.pack()
# root.mainloop()


# Je trouve vraiment ca ridicule de mettre ces etapes, cuz 
# donnees yo trop incomprehensibles