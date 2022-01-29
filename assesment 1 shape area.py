ch=int(input("Enter 1 for square \nEnter 2 for rectangle \nEnter 3 for triangle \nEnter 4 for circle"))
if(ch==1):
    s=float(input("Enter a side"))
    print("Area of square is...",s*s)
elif(ch==2):
    l=float(input("Enter the length"))
    b=float(input("Enter the breadth"))
    print("Area of a rectangle is...",l*b)

elif(ch==3):
    l=float(input("Enter the length"))
    n=0.5
    h=float(input("Enter the height"))
    print("Area of a triangle is...",n*l*h)
elif(ch==4):
    r=float(input("Enter the radius"))
    pi=3.141592653579
    print("Area of a circle is...",r*r*pi)
else:
    print("Error, you have not entered an available option and now corporate is after you.")
    
          
