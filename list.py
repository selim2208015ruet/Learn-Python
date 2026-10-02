i=0
sum=0
list = []
for i in range(5):
    num = int(input("Enter your number= "))
    list.append(num)
    sum=sum+num
    i+=1


print("Numbers= ",list)

print("sum= ", sum)

largest = list[0]
for num in list:
    if num>largest:
        largest=num

print("largest= ",largest)
    
