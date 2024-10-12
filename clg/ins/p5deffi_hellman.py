# from random import randint
p=23
g=9
a=4
b=6

print("the siogret key p and g is: ",p,g)
print("the sigret key of person1 is: ",a)
print("the sigret key of person2 is: ",b)

x = int(pow(g,a,p))
y = int(pow(g,b,p))

ka = int(pow(y,a,p))
kb = int(pow(x,b,p))

print("key of person 1 is : ",ka)
print("key of person 2 is : ",kb)