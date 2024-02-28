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

# the range() function can accept to args (min, max) and generate a simple numeric tange between min and max with an increment
# of 1.
print(range(20, 30))
# Convert the generated range object into a list to see the full list of numbers.
print(list(range(100)))


print()
print()
# Example 1
# Generate a range between 40 and 80.
# From that range, capture the numbers that are only divisible by 7 into a new list by multiplying them by 2.
range1 = range(40, 80)
list1 = list(range1)
print(list1)



extract1 = [ num * 2 for num in range1 if num % 7 == 0 ]
print(extract1)

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


# any()  - In a boolean iterable, if the function any() finds a True, the output  will be True. Else, False.
# all() - In a boolean iterable, if the function all() finds all values to be True, the output  will be True. Else, False.


def run_password_checker(num_attempts = 1):
    print("######### PASSWORD CHECKER ##########")

    if num_attempts < 1 | num_attempts > 5:
        print("Invalid number of attempts.")
        return None

    for attempt in range(1, num_attempts + 1):
        print("ATTEMPT ", attempt)
        u_password = input("Enter the password to check: ")
        conditions = {'LENGTH': False, 'UPPERCASE': False, 'LOWERCASE': False, "DIGIT": False }

        if len(u_password) >= 8:
            conditions['LENGTH'] = True

        for char in u_password:
            if char.isupper() and not(conditions['UPPERCASE']):
                conditions['UPPERCASE'] = True
            elif char.islower() and not(conditions['LOWERCASE']):
                conditions['LOWERCASE'] = True
            elif char.isdigit() and not(conditions['DIGIT']):
                conditions['DIGIT'] = True

        print("Password Test")
        print(conditions)

        if all(conditions.values()):
            print("Password Meets All Requirements.")
            break;
        else:
            print("One or More Password Requirements Were Not Met.")

print()
# run_password_checker(3)

#user_input = input("Provide a Password: ")
#print(user_input)

print()
print()
# While
# while the email count is less than 10, send a random SMAP email.
email_count = 1

while email_count <= 10:
    print("Sending the SAMP: ", email_count)
    email_count += 1

# Send a random SMAP to the users with odd userID (userID is from 1 to 20)
print()
print()
print()
userID = 0

while userID < 20:
    userID += 1
    if userID % 2 == 0:
        continue

    print("Sending the SAMP: ", userID)

""" 
Write a function in Python (generate_fibonacci) to accept one integer argument (n) and 
generate the Fibonacci series of  n numbers. The series shall start at 1. 
A sample Fibonacci series of 7 numbers: 1, 1, 2, 3, 5, 8, 13
Show the application of these functions.
"""

def generate_fibonacci(n):
    print()
    print("####### Fibonacci Series for the first ", n, " numbers #######")
    fib = []
    counter = 0

    while counter < n:
        if counter == 0 or counter == 1:
            fib.append(1)
        else:
            fib.append(fib[counter - 1] + fib[counter - 2])

        counter += 1

    return  fib

print(generate_fibonacci(2))
print(generate_fibonacci(5))
print(generate_fibonacci(20))