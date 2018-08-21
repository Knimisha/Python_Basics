class Parent:                   # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentfunc(self):
        print("Calling parent function")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttrNimisha(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):           # define child class

    def __init__(self):
            print("Calling child constructor")

    def childfunc(self):
            print("Calling child function")


c = Child()                     # instance of child
c.childfunc()                   # child calls its method or function
c.parentfunc()                  # calls parent's method
c.setAttr(100)                  # calling parent's method again
c.getAttrNimisha()              # calling parent's method again
