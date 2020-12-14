test_str = "GeeksforGeeks"
  
# printing original string  
print("The original string is : " + str(test_str)) 
  
# using join() + bytearray() + format() 
# Converting String to binary 
s = ''.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8')) 
  
# printing result  
print("The string after binary conversion : " + str(s)) 
print (''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8)))