# Gates
# NOT
import random

print(1000> 2000)
print(not(1000> 2000))

a = random.uniform(10,100) # a is a random number from the uniform distribution where min = 10 and max = 100
b = random.normalvariate(60 , 5) # b is a random number from the normal distribution where mean/average = 60 and standard dev. = 5

print(a)
print(b)

if a > b:
    print("A")
else:
    print("B")

if not(a > b):
    print("Z")
else:
    print("X")


# network_load and device_type: two variables
# if the network_load is greater or equal to 5000 mbs and the device_type is 1 then print "Heavy"
# if the network_load is less than 5000 mbs or greater than or equal to 1000 and device_type is 1 print "Moderate"
# if the network_load is greater than or equal to 10,000 mbs and device_type is 2 print "Critical"
# In all other cases, print "Normal"
print()
print("###### NETWROK DEVICE DASHBOARD #######")
device1 = {"deviceID": "0001", "network_load": random.uniform(500, 15000), "device_type": round(random.uniform(1,3))}
print(device1)

"""
if conditional_expression_1:
    do something
elif conditional_expression_2:
    do something
elif conditional_expression_3:
    do something
else:
    do something

exp1 and exp2;
exp1 or exp2;

"""

if device1["network_load"] >= 5000 and device1["device_type"] == 1:
    print("Heavy")
elif device1["network_load"] < 5000 and device1["network_load"] >= 1000  and device1["device_type"] == 1:
    print("Moderate")
elif device1["network_load"] >= 10000 and device1["device_type"] == 2:
    print("Critical")
else:
    print("Normal")


print()
print()
if a > 50 : print("WELL DONE!!!")
print("Great Job!!") if a > 50 else print("Hmmmm... Try Again.")
print("Great Job!!") if a > 75 else print("Good Job!!") if a > 50 else print("Hmmmm... Try Again.")

person = "Tony"
approved_names = {"Harry", "Bob", "Tom", "Dick"}

if person in approved_names:
    print("ACCESS GRANTED")
else:
    print("GET LOST!!")

"""
The in operator in Python is used to check if a value is present in a sequence, 
such as a string, list, tuple, or set. 
It returns True if the value is found in the sequence, and False otherwise.
"""



# Loops
bandwith_allowance = [600, 700, 800, 400, 200, 150, 700]
"""
Person 1 Bandwith: 600
Person 2 Bandwith: 700
...
...
"""

print()
print()
counter = 1
for bandwith in bandwith_allowance:
    print("Person", str(counter), "Bandwith: ", str(bandwith))
    counter += 1

text1 = "HappyBirthday190"

have_upper = False

for char in text1:
    if(char.isupper()):
        have_upper = True
        print("An Upper Case Character was Found.")
        break; # Exit the entire loop


# List Comprehension - for each character in text1, if the character is an upper case character, collect that into a new list.
# Generate a new list with Upper Case characters in text1.
print([ char for char in text1 if char.isupper()])

# continue; # Break the current iteration of a loop

########## BONUS ACTIVTY 1: THIS WILL GRANT YOU 4 BONUS POINTS FOR TEST 1 ##########
""" 
Password Strength Checker
Write a Python program (function) that takes a user-input password and checks its strength based on 
the following criteria:

At least 8 characters long
Contains a mix of uppercase and lowercase letters
Contains at least one digit (0-9)
"""

#user_input = input("Provide a Password: ")
#print(user_input)

