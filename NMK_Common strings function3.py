# replace replaces part of the string
# find finds a string into another string
# split splits string on behalf of splitter

String1 = "www.gmail.com"
print(String1.replace("gmail","ymail"))

# find how many characters exist in the string
z = 0
for i in String1:
    if (i == 'l'):
       z += 1

print(z)


#alternative to above example

x = len(String1)
y = len(String1.replace("l", ""))

print(x-y)

# example of find. If the return value is -1 then it means the string is not found
z = "gmail"
print(String1.find(z))


# example of split
String2 = "India is my country. I love my country"
list1 = String2.split(" ")
print(len(list1))
print(list1)