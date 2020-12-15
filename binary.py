import numpy as np

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def binaire_to_ternaire(binaire):
    temp  = [int(x) for x in  list(bits)]
    Ternaire = [-1 if x==0 else 1 for x in temp]    
    return Ternaire

def pop_zeros(items):
    while items[-1] == 0:
        items.pop()
    return items

def ternaire_to_binaire (ternaire):
    temp = pop_zeros(ternaire)
    temp1 = [0 if x==-1 else x for x in temp] 
    temp2 = [str(i) for i in temp1]
    ternaire = ''
    ternaire = ternaire.join(temp2)
    return ternaire

def padding (message1,message2):
    difference = len(message1) - len(message2)
    if difference > 0 :
        for i in range (difference):
            message2.append(0)
    elif difference < 0:
        for i in range (-difference):
            message1.append(0)

    return message1,message2


text = "texte de test"
bits = text_to_bits(text)
text_back = text_from_bits(bits)

tosend = binaire_to_ternaire(bits)


toreceive = ternaire_to_binaire(tosend)

converted = text_from_bits(toreceive)

print (tosend)

mes1 = [1,-1,1,1,1,-1]
mes2 = [1,-1]
text1,text2 = padding(mes1,mes2)

