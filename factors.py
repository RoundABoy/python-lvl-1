num=int(input("Enter a number: "))
factor=1
while(factor<=num):
  if(num%factor==0):
      print("The factor is...",factor)
  factor+=1
