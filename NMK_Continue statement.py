number = input("enter the number")
number = int(number)

for i in range(1, 11):

    if ((number * i) % 10 == 0):
        continue
    print(number * i)