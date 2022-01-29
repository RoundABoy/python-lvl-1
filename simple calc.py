a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
ch=int(input("Enter 1 for addition \nEnter 2 for Subtraction \nEnter 3 for multiplication \nEnter 4 for division \nEnter 5 for the remainder" ))
if(ch==1):
    print("The addition of these numbers is...",a+b)
elif(ch==2):
    print("The difference of these numbers is...",a-b)
elif(ch==3):
    print("The product of these numbers is...",a*b)
elif(ch==4):
    print("The coefficent of these numbers is...,",a/b)
elif(ch==5):
    print("The remainder of these numbers is...",a%b)
else:
    print("Error, corporate is now after you")

