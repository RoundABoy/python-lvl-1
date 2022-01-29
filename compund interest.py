p=float(input("Enter the amount of money"))
r=float(input("Enter the rate"))
t=float(input("Enter the time"))
ch=int(input("Enter 1 for simple interest \nEnter 2 for compound interest"))
if(ch==1):
    print("simple interest is...",p*r*t/100)
elif(ch==2):
    amount=p*(pow((1+r/100),t))
    ci=amount-p
    print("compound interest is...",ci)
else:
    print("Invalid option please try again.")
