import random
import string
from shlex import join


def generate_password(length,UpperCase,LowerCase,Numbers,Symbols):
    character=''
    if UpperCase:
        character += string.ascii_uppercase
    if LowerCase:
        character += string.ascii_lowercase
    if Numbers:
        character += string.digits
    if Symbols:
        character += string.punctuation
    if not character:
        print("Character Not Found")



    password =''.join(random.choice(character) for ln in range(length))
    return password





length =int(input("how mush length want password : "))
UpperCase=input("do you want UpperCase Yes/No:").lower() =='yes'
LowerCase=input("do you want LowerCase Yes/No:").lower() =='yes'
Numbers=input("do you want Numbers Yes/No:").lower() =='yes'
Symbols=input("do you want Symbols Yes/No:").lower() =='yes'

password=generate_password(length,UpperCase,LowerCase,Numbers,Symbols)
print(password)


