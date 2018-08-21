class Mathematics1:

    def __init__(self):
        print("Contructor")
        #print("the roll number is", x1+y1)

    def add(self, x, y):
        print("The sum of the two number is", x+y)

    def mult( self, x1, y):
        print("The product is", x1 * y)

    def sub(self, x,y):
        print("The result is", x-y)

class Mathematics2(Mathematics1):

    def sub(self, x,y):
        print("The result is", y-x)


obj = Mathematics1()
obj.add(10, 20)
obj.mult(24,56)
obj.sub(56,24)


