a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a>b and a>c):
    print(a,"is greatest number among three.")
elif(b>c):
    print(b,"is greatest number among three.")
else:
    print(c,"is greatest number among three.")