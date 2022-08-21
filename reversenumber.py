#reverse a number
n = int(input("please give a number:"))
print("before your reverse your number is : %d" %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10
    n = (n//10)
    print("after reverse : %d" %reverse)