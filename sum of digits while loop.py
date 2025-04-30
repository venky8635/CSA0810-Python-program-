n=int(input("enter number : "))
sumofdigits=0
while(n>0):
    sumofdigits=sumofdigits + n %10
    n //= 10
print(sumofdigits)
