# import substitution and transposition cipher

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)  

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result+= chr((ord(char)-s-65)%26+65)
        else:
            result+= chr((ord(char)-s-97)%26+97)
    return result


text = input("Enter a Text to encrypt: ")
s = 15  # default secure key
print("Text : ", text)
print("Cipher : ", decrypt(text, s))
