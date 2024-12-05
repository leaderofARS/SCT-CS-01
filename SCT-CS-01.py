alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,shift_key): #hello h=?
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text += char    
    print(f"Here is the text after encryption: {cipher_text}")    

def decryption(cipher_text,shift_key): #khoor h=?
    plain_text=""
    for char in cipher_text: #char=k
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text +=alphabet[new_position]
        else:
            plain_text += char    
    print(f"Here is the text after decryption: {plain_text}")   
want_to_end=False
while not want_to_end:
    what_to_do=input("Type 'Encrypt' for encryption, Type 'Decrypt' for decryption:\n")
    text=input("Type your message:\n")
    shift=int(input("Enter the shift key:\n"))
    if what_to_do=="Encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="Decrypt":
        decryption(cipher_text=text,shift_key=shift)    
    play_again=input("Type 'yes' to continue ,Type 'no' to exit")
    if play_again=='no':
        want_to_end=True
        print("Good Coding ! Bye.....")