n=int(input("enter number:"))
sum=0
for i in range(1,n,1):
    if(n%i==0):
        print("the number is perfect")
    else:
        print("the number is not perfect")
