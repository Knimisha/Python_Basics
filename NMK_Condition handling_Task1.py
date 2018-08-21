# Program to find the largest number among the three numbers

class largest():

    def condition(self):
        inputA = input ( "Enter the first number" )
        inputA = int ( inputA )
        print ( "The first number is" , inputA )
        inputB = input ( "Enter the second number" )
        inputB = int ( inputB )
        print ( "The second number is" , inputB )
        inputC = input ( "Enter the third number" )
        inputC = int ( inputC )
        print ( "The third number is" , inputC )

        if(inputA > inputB and inputA > inputC):
            print("The largest number is", inputA)
        elif(inputB > inputA and inputB > inputC):
            print("The largest number is", inputB)
        elif(inputA == inputB or inputA == inputC):
            print("Invalid condition")
        else:
            print("The largest number is", inputC)

obj = largest()
obj.condition()