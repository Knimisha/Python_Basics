inputNum = input("Enter the number")
inputNum = int(inputNum)

if (inputNum >= 0):
    if (inputNum % 2 == 0):
        print("Entered number is even")
    else:
        print("Entered number is odd")
else:
    print("Warning: Entered number is negative")
