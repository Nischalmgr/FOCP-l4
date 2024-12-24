'''Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.'''
def encrypts(message):
    no_spaces=message.replace(" ","")
    encrypt_msg=no_spaces[::-1]
    return encrypt_msg
if __name__=="__main__":
    msg=input("enter the message: ")
    encrypt=encrypts(msg)
    print(f"The original message:{msg}\n Encrypted message:{encrypt}")