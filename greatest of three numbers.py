a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>b):
    if(a>c):
        print("the greatest number is:",a)
    else:
        print("the greatest number is :",c)
else:
    if(b>c):
      print("the greatest number is:",b)
    else:
        print("the greatest number is:",c)
