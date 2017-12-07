cipher_text = raw_input("enter cipher text here ---->   ")

key = raw_input("enter the key --->  ")
plain_text = []
for letter in cipher_text:
     
    pt_number = ord(letter) 
      
    if 97 > pt_number < 122:
        plain_text.append(letter)    
     
    else:
        pt_number += int(key)
        
        if pt_number > ord("z"):
            pt_number = pt_number - 26
            plain_text.append(chr(pt_number))
        
            
        else:
            pt_number = ord(letter) + int(key)
            plain_text.append(chr(pt_number))
        
    

else:
    print ''.join(plain_text)
