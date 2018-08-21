# program to check whether a number is divisible by 5 and 11 or not


class div():

    def division(self, inputA):
        if(inputA % 5 == 0 and inputA % 11 != 0):
            print("Number divisible only by 5")
        elif(inputA % 5 != 0 and inputA % 11 == 0):
            print("Number is divisible by 11")
        elif(inputA % 5 == 0 and inputA % 11 == 0):
            print("The number is divisible by both")
        else:
            print("Better luck next time")

obj = div()
obj.division(20)



