num = int(input("Enter your Number: "))

if num>0 and num%2==0:
    print("Positive Even")

elif num>0 and num%2!=0:
    print("Positive Odd")

elif num<0:
    print("Negative")

elif num==0:
    print("Zero")