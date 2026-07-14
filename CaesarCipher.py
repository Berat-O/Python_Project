def encrypt(message,shiftNumber):
    letters='abcdefghijklmnopkrstuvwxyz'
    letterslist=[]
    for letter in letters:
        letterslist.append(letter)


    messagelist=[]
    for letter in message.lower():
        messagelist.append(letter)
    
    encryptedList=[]
    for letter in messagelist:
        if letter in letterslist:
            x=letterslist.index(letter)
            x=(x+shiftNumber)%len(letterslist)
            encryptedList.append(letterslist[x])
        else:
            encryptedList.append(letter)
    encryption="".join(encryptedList)
    print(f"Here is your encoded result: {encryption}")

def decrypt(message,shiftNumber):
    letters='zyxwvutsrqponmlkjihgfedcba'
    letterslist=[]
    for letter in letters:
        letterslist.append(letter)


    messagelist=[]
    for letter in message.lower():
        messagelist.append(letter)
    
    decryptedList=[]
    for letter in messagelist:
        if letter in letterslist:
            x=letterslist.index(letter)
            x=(x+shiftNumber)%len(letterslist)
            decryptedList.append(letterslist[x])
        else:
            decryptedList.append(letter)
    decryption="".join(decryptedList)
    print(f"Here is your decoded result: {decryption}")

print("*****Welcome to the Caesar Cypher!*****")
value=1
while value==1:
    choice=input("Type 'encode' to encrypt\n Type 'decode' to decrypt: \n")

    if choice=='encode':
        Message=input("Type your message: ")
        shift=int(input("Type the shift Number: "))
        encrypt(Message,shift)

    elif choice=='decode':
        Message=input("Type your message: ")
        shift=int(input("Type the shift Number: "))
        decrypt(Message,shift)
    else:
        print("Invalid Input")

    again=input("Type 'yes' if you want go again otherwise 'no': ")
    if again=='yes':
        value=1
    else:
        value=0
        print("Good Bye")
