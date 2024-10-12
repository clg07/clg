import hashlib
msg=input("Enter a msg : ")
result = hashlib.sha1(msg.encode())
print("hexadecimal equivaleent of sha1 is: ")
print(result.hexdigest())