
#Cas 1 : 1 utilisateur et abscence de Bruit
print('1 utilisateur et abscence de Bruit')
Key_1           = Walsh[2] 
Message_User_1  = [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1]
Spreaded        = Message_Spreader(Message_User_1)
Encoded         = Message_Encoder (Spreaded , Key_1)
Encoded_to_Volts= [i * -1 for i in Encoded ] # 1 => -1 volt ,0 = 0 voly and -1 = 1 volt
Traffic         = Encoded_to_Volts # 1 user et pas de bruit 
Received        = Decoder(Traffic,Key_1)
Error           = BER(Message_User_1,Received)
print ("Input :",Message_User_1)
print ("Output: ", Received)
print ('BER :',Error)

print ()

#Cas 2 :  1 utilisateur et presence de Bruit
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

print ()
#Cas 4 : 2 utilisateur et Presence de Bruit
print('2 utilisateur et Presence de Bruit')
Key_1               = Walsh[2] 
Key_2               = Walsh[3]
Message_User_1      = [1,-1,1,1,1,-1]
Message_User_2      = [-1,-1,1,1,1,0]

Spreaded_1          = Message_Spreader(Message_User_1)
Spreaded_2          = Message_Spreader(Message_User_2)

Encoded_1           = Message_Encoder (Spreaded_1 , Key_1)
Encoded_2           = Message_Encoder (Spreaded_2 , Key_2)

Encoded_to_Volts_1  = [i * -1 for i in Encoded_1 ] # 1 => -1 volt ,0 = 0 volt and -1 = 1 volt
Encoded_to_Volts_2  = [i * -1 for i in Encoded_2 ]
Noise               = Noise_Generator(len(Spreaded_1))
Traffic             = Multiplexing(Encoded_to_Volts_1 ,Encoded_to_Volts_2,Noise)

Received_1          = Decoder(Traffic,Key_1)
Received_2          = Decoder(Traffic,Key_2)

Error_1             = BER(Message_User_1,Received_1)
Error_2             = BER(Message_User_2,Received_2)
print ("Input User 1 :",Message_User_1)
print ("Output User 1: ", Received_1)
print ('BER :',Error_1)
print ()

print ("Input User 2 :",Message_User_2)
print ("Output User 2: ", Received_2)
print ('BER :',Error_2)

# print ()
# print (Traffic)
# print ()
# print (Message_User_1)
