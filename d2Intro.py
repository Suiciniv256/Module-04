# Numeric Data
import random

x = 1
y = 35656222554887
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.45
y = 35.656222554887
z = -32.55522

print(type(x))
print(type(y))
print(type(z))

str1 = "Hello Ability, How are you?"
print(str1, "\n")

str2 = """Hello Ali, How are you?
It's been a long day. 
I know that it is so sunny."""

print(str2, "\n");

# length of any data object
print(len(str2), "\n");

# Search if Ali is in the given string
print("Ali" in str2)

# Search if Ali is in the given string
print("Ali" not in str2)

print()
if "Ali" in str2:
    print("Oh Hey, Ali")
else:
    print("I miss Ali")


# [3, 4, 6, 8, 9, 10, 14, 16, 16, 18]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]


print()
str3 = "Happy Birthday, Clement!!!"
print(str3[0])
print(str3[0:5]) #[0,5)
print(str3[6:14]) #[6,14)

print(str3[:5]) #[0,5)
print(str3[6:]) #[6,last char]

print(str3[-5:])
print(str3[21:])



"Clement"
"Birthday, Clement"

"!!!"
print(str3[-3:])

"Clement"
print(str3[-10:-3])

"Birthday, Clement"
print(str3[6:-3])


#Boolean
print()
True; False
print("Ali" in str2)
print()


#Casting
a1 = 0
a2 = 1
a3 = 5
a4 = -9

print(bool(a1))
print(bool(a2))
print(bool(a3))
print(bool(a4))


s1 = "True"
s2 = "False"
s3 = "Camila"
s4 = "TRUE"
s5 = "FALSE"
s6 = "0"


print()
print(bool(s1))
print(bool(s2))
print(bool(s3))
print(bool(s4))
print(bool(s5))
print(bool(s6))

print()
print()
# Operators
n1 = 89
n2 = 5

print(n1 + n2)
print(n1 - n2)
print(n1 / n2)
print(n1 * n2)
print()
print(n1 % n2)
print(n1 // n2)
print(n1 ** 2)
print(n1 ** n2)

print()
print(n1)
n1 += 5 #n1 = n1 + 5
print(n1)
n1 *= 4


#11111
#01010
#bit AND
#01010


#11111
#01010
#bit OR
#11111

#4 - 100 (bit-wise)
"""000 - 0
001 - 1
010 - 2
011 - 3
100 - 4
101 - 5
110 - 6
111 - 7"""
print()
print("Bitwise AND")
print(4 & 5)

print("Bitwise OR")
print(4 | 5)

print()
x = random.uniform(10, 20)
print(x)

import random
from random import uniform