inputNumber = input("Enter the number")
inputNumber = int(inputNumber)

if (inputNumber < 0):
    print("The number entered is negative")
elif (inputNumber == 0):
    print("The number cannot be zero")
elif (inputNumber%2 ==0):
    print("The number entered is an even number")
else:
    print("The number entered is an odd number")