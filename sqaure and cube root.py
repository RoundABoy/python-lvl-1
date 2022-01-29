num=int(input("Enter a number: "))
ch=int(input("Enter 1 for square root \nEnter 2 for the cube root: "))
a=num**(1/2)
if(ch==1): 
   print("The sqaure root is",a)
elif(ch==2):
   b=num**(1/3)    
   print("The cube root is",b)
else:
    print("Error")
