a = "Testing"
b = "Testing"

if (a == b):
    print("Match found")
else:
    print("Not found")


# if the strings are same but there are spaces then strip function can be used
c = "Testing1"
d = "      Testing1       "

if (c.strip() == d.strip()):
    print("Found")
else:
    print("Not found")


# if the strings are in different cases (upper and lower)
e = "Hello"
f = "hello"

if(e.lower() == f.lower()):      # if (e.upper() == f.upper()): is also an alternative
    print("Found")
else:
    print("Not found")


# reversing a string
g = "Testing world"
h = ""

l = len(g)

for i in range ((l-1), -1, -1):
    #print(g[i])                #printing reverse
    h = h + g[i]

print(h)

# palendrome
string3 = "madam"
string4 = ""

len1 = len(string3)
for i in range((len1 - 1), -1, -1):
    string4 = string4 + string3[i]

print(string4)

if (string3 == string4):
    print("Its a palendrome")
else:
    print("Sorry! wrong string")
