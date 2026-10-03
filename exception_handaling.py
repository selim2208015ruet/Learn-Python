try:
    num = int(input("Enter a Number: "))
    print("You entered: ",num)

except ValueError:
    print("Invaliid input! please enter a number")