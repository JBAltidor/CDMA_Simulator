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

def ternaire_to_binaire (ternaire):
    #remove appending zeros
    temp = [0 if x==-1 else x for x in ternaire] 
    ternaire = ''
    


text = "texte de test"
bits = text_to_bits(text)
text_back = text_from_bits(bits)

print (text)
print (bits)

print (binaire_to_ternaire(bits))
# print (Converted)
# print (binaire_to_ternaire(bits))
print (text_back)