y=int(input("enter a number: "))
factorial=1
if(y<0):
    print("Error, deal with it")
elif y==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,y+1):
        factorial=factorial*i
    print("The factorial of",y,"is",factorial)
