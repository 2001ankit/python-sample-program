size=int(input("Enter the number of array you want to array in element :"))
arr=[]
for i in range (0,size):
    elem = int(input("please give value for index "+str(i)+": "))
    arr.append(elem)
avg=sum(arr)/size
print("Average of the array element is ",avg)

