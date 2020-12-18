import numpy as np
import random

#Constantes
Walsh = np.array([[1,  1,  1,  1,  1,  1,  1,  1],
[1, -1,  1, -1,  1, -1,  1, -1],
[1,  1, -1, -1,  1,  1, -1, -1],
[1, -1, -1,  1,  1, -1, -1,  1],
[1,  1,  1,  1, -1, -1, -1, -1],
[1, -1,  1, -1, -1,  1, -1,  1],
[1,  1, -1, -1, -1, -1,  1,  1],
[1, -1, -1,  1, -1,  1,  1, -1]])

B = 0.2

#------------------------------------------------------------------------------#

def Message_Spreader(message):
    #Etale le message sur longeur message * longueur code de Walsh
    Spreaded = []
    for i in range (len(message)):
        for j in range (0,8):
            Spreaded.append(message[i])
    return Spreaded

def Message_Encoder (Spreaded , key):
    #fait un XOR entre le message etale et le code de Walsh de l'utilisateur
    Encoded = []
    for i in range (len(Spreaded)):
       result = xor(Spreaded[i] , key[i% len(key)])
       Encoded.append(result)
    return Encoded

def xor (a,b):
    #Redefinition de l'operation xor en tenant compte des "-1"
    if a == 0 or b == 0:
        return 0
    elif (a == b):
        return -1
    return 1

def Noise_Generator(size):
    #Genere un bruit aleatoire de la meme longueur que le message
    Noise = []
    for i in range (0,size):
        Noise.append(B*random.randint(-1,1))
    return Noise

def Multiplexing (User_1 , User_2 , Noise):
    #Melange les signaux pour la transmission
    Traffic = []
    for i in range (0,len(User_1)):
        Traffic.append(User_1[i] + User_2[i] + Noise[i])
    return Traffic

def Multiplexing_2 (User_1 , Noise):
    Traffic = []
    for i in range (0,len(User_1)):
        Traffic.append(User_1[i] +  Noise[i])
    return Traffic

def Decoder(Traffic , key):
    #Recupere les message a la reception 
    Decoded = []
    for i in range(0, len(Traffic), 8):
        temp= Traffic[i:i + 8]
        result = np.inner(temp,key)
        Decoded.append(result/8)      
    Received =[round(x) for x in Decoded]
    return Received

def BER (Input , Output):
    #Calcule le Bit Error Rate
    error = 0
    for i in range (0,len(Input)):
        if Input[i] != Output[i]:
            error  += 1
    return error/len(Input)

#--------------------------------------------------------------------------------------#

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    #Convertit un texte en train binaire
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    #Convertit un train binaire en texte
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def binaire_to_ternaire(binaire):
    #Convertit un train binaire en train ternaire (-1,0,1)
    temp  = [int(x) for x in  list(bits)]
    Ternaire = [-1 if x==0 else 1 for x in temp]    
    return Ternaire

def pop_zeros(items):
    #Permet de retirer les zeros ajoutes comme padding
    while items[-1] == 0:
        items.pop()
    return items

def ternaire_to_binaire (ternaire):
    #Convertit un train ternaire en train binaire
    temp = pop_zeros(ternaire)
    temp1 = [0 if x==-1 else x for x in temp] 
    temp2 = [str(i) for i in temp1]
    ternaire = ''
    ternaire = ternaire.join(temp2)
    return ternaire

def padding (message1,message2):
    #Permet de ramener les messages a une meme longueur
    difference = len(message1) - len(message2)
    if difference > 0 :
        for i in range (difference):
            message2.append(0)
    elif difference < 0:
        for i in range (-difference):
            message1.append(0)

    return message1,message2
#__________________________________________________________________________________________________#

#Driver code
if __name__ == "__main__":
    print ("\t \t Code Division Multiple Access-Simulation\n")
    print ("*(1) 1 Utilisateur et presence de bruit.\n*(2) 1 Utilisateur et absence de bruit.\n*(3) 2 Utilisateurs et presence de bruit.\n*(4) 2 Utilisateurs et absence de bruit.\n")
    choix = input ("> Choisissez le numero de votre option : ")

    if (choix == 1):
        #1 Utilisateur et presence de bruit
        print('1 utilisateur et presence de Bruit')
        Key_1           = Walsh[2] 
        Message_User_1  = [1,-1,1,1,1,-1]
        Spreaded        = Message_Spreader(Message_User_1)
        Encoded         = Message_Encoder (Spreaded , Key_1)
        Encoded_to_Volts= [i * -1 for i in Encoded ] # 1 => -1 volt ,0 = 0 volt and -1 = 1 volt
        Noise           = Noise_Generator(len(Spreaded))
        Traffic         = Multiplexing_2(Encoded_to_Volts,Noise)
        Received        = Decoder(Traffic,Key_1)
        Error           = BER(Message_User_1,Received)
        print ("Input :",Message_User_1)
        print ("Output: ", Received)
        print ('BER :',Error)


    elif (choix == 2):
        #1 Utilisateur et absence de bruit.

    elif (choix == 3) :
        #2 Utilisateurs et presence de bruit.

    elif (choix == 4) :
        #2 Utilisateurs et absence de bruit.


    else :
        exit ()
