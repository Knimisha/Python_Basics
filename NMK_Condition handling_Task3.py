# Program to check whether the triangle is equilateral, scalene, or isosceles

class traingle():
    def tri(self, A, B, C):
        A = int(A)
        print("First side of the triangle is", A)
        B = int(B)
        print("Second side of the triangle is", B)
        C = int(C)
        print("Third side of the triangle is", C)
        if(A == B and A ==C and B == C):
            print("Its an equilateral triangle")
        elif(A == B and A != C and B != C):
            print("Its an isosceles triangle")
        else:
            print("Its scalene triangle")

obj = traingle()
obj.tri(11, 11, 13)