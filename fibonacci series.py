a=0
b=1
n=int(input("enter number :"))
print("fibonacci series : ")
print(a,b)
for i in range(2,n,1):
    c=a+b
    print(c)
    a=b
    b=c
