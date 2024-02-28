# Functions

def calculateSalary(hours, hWage, bonusApllied):
    """

    :param hours: hours of work performed
    :param hWage: hourly wage
    :param bonusApllied: a flag (bool) indicating if a bonus is applied
    :return: salary
    """
    salary = hours * hWage

    if (bonusApllied):
        salary *= 1.1

    return salary


person1Salary = calculateSalary(20, 15, False)
person2Salary = calculateSalary(12, 16, True)

print("Salaries of Workers")
print("Person 1:", person1Salary)
print("Person 2:", person2Salary)
print("Person 2:", calculateSalary(90, 100, True))

""" 
Write a function to accept two parameters and return the following value:
Param 1: Name
Param 2: FavAnimal
Return: Name’s Favorite Animal is FavAnimal. 
"""


def concat_fav_animal(name, fav_animal):
    return name + "’s Favorite Animal is " + fav_animal


print(concat_fav_animal("Tony", "Cat"))
print(concat_fav_animal("Bailey", "Parrot"))

"""
Write a function to accept marks of 4 subjects and return the average.
"""


def calculate_avg(m1, m2, m3, m4):
    return (m1 + m2 + m3 + m4) / 4


def calculate_avg2(m1, m2, m3, m4):
    avg = (m1 + m2 + m3 + m4) / 4
    return avg


print(calculate_avg(45, 67, 89, 90))
print(calculate_avg(90, 87, 89, 90))

print(concat_fav_animal("Tony", "Cat"))
print(concat_fav_animal("Cat", "Tony"))
print(concat_fav_animal(fav_animal="Cat", name="Tony"))


def concat_fav_animal2(name, fav_animal="Dog"):
    return name + "’s Favorite Animal is " + fav_animal


print(concat_fav_animal2(name="Camila"))
print(concat_fav_animal2(name="Camila", fav_animal="Cat"))

"""
If the total Packet Size (header + body+ trailer)  is greater than 1000,
then this is an abnormal packet. If not, this is a normal packet.

Write a function to similuate this situation. 
"""

print()
print("PACKET VERIFICATION")


def verify_packet(header: float, body: float, trailer: float) -> str:
    total_size = header + body + trailer
    if (total_size > 1000):
        return "ABNORMAL PACKET"
    else:
        return "NORMAL PACKET"


print("Packet 1:", verify_packet(700, 100, 50))
print("Packet 2:", verify_packet(1000, 240, 900))


def do_something_stupid():
    pass


print()
print("Lamda")

lam1 = lambda a : a**4 + 900
print(lam1(3))

""" As same as the following:
def lam1(a):
    return a**4 + 900
"""

lam2 = lambda a, k : a**k + 900
print(lam2(3,2))
