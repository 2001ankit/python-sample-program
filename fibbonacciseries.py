


first,second=0,1
n=int(input("please give a number"))
print("fibonacci series are:")
for i in range(0,n):
    if i<=1:
        result=i
    else:
     result=first+second;
     first=second;
     second=result;
    print(result)
    
a=int(input("Enter first number"))
b=int(input("Enter second number"))
n=int(input("enter a number"))
print(a,b,end="")
while n-2:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
