# Tuples
devices = ("Printer", "Switch", "Monitor", "Router")
print(devices)
print(type(devices))
print(len(devices))
print(devices[1])

# devices[1] = "Workstation"

devices_list = list(devices)
print(devices_list)
devices_list[1] = "Workstation"
devices_2 = tuple(devices_list)
print(devices_2)

devices_3 = devices + devices_2
print(devices_3)
print(devices)

print("Workstation" in devices_3)
print()
print(devices)

(d1, d2, d3, d4) = devices
print(d1)

(d1, *dn) = devices
print(d1)
print(dn)

"""
We have a tuple with contains lists of some employees.
	employee_details = [(1, "AA", 100),(1, "BB", 1001),(1, "cc", 1002)]
How would you access the details of 2nd employee?
How would you print the name of the second employee?
"""
employee_details = [(1, "AA", 100),(1, "BB", 1001),(1, "cc", 1002)]
print(employee_details)
print(type(employee_details))
print(type(employee_details[1]))
print(employee_details[1])
print(employee_details[1][1])

"""
Consider:
		student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
If student_id keys were to be stored separately, what would be the most suitable data structure and why? 
"""

# Set
names1 = {"Beiley","Tony", "Steve", "Cena", "Gabe"}
names2 = {"Shana","Gil","Genavive","Cena", "Gabe"}

print(names1)
print(names2)

names1.add("Gabe")
print(names1)

names3 = {"Rahman","Kate","Kate","Kate"}
print(names3)

print()
print(names1)
print(names2)
names1.update(names2)
print(names1)

""" 
 The company Set have 6 clients and the countries of the clients are put in the set as follow:
 Countries = {Brazil, USA, Canada, Colombia, Mexico, England}
All the clients from USA decided to move the operations to Canada. How to update the set?
"""
print()
Countries = {'Brazil', 'USA', 'Canada', 'Colombia', 'Mexico', 'England'}
print(Countries)
Countries.remove('USA')
print(Countries)

"""
Imagine you are building an invitation list where people can come out to the viewing of new villa . 
To keep track of a user's invited, you can use a set data structure to store the unique IDs of the users 
that are going to come. 
Represent this data by using a set.
You have a user that you want to remove from the set. how would you do that?
There is another set that you maintained for a previous party. 
How would you determine the set of people who were invited for both events. 
"""

event1 = {"U1", "U2", "U3", "U4" , "U5", "U6", "U7"}
event0 = {"U1", "U7", "U6", "U4", "U8", "U9", "U10", "U11" }

print(event1)
print(event0)

event1.remove("U2")
both_events = event1.intersection(event0)
print(both_events)

# Dictionary
web1 = { "name" : "facebook.com",
         "number_of_pages" : 50,
         "home_link" : "http://www.facebook.com",
         "type": "Social"
}

web2 = { "name" : "toronto school of management",
         "number_of_pages" : 45,
         "home_link" : "http://www.torontosom.ca",
         "type": "Edcuation"
}

print(web1)
print(web2)

print(len(web1))

web3 = dict(
            name = "X",
         number_of_pages  = 67,
        home_link = "http://www.X.com",
         type = "Social"
)

websites = [web1,web2,web3]
print(websites)

web3["number_of_pages"] = 78
print(web3)

web3["last_visit"] = "01/01/2023"
print(web3)

web3.update({"last_update" : '01/02/2023', "monthly_avg_visits": 5678530})
print(web3)

""" 
Extract the brand from the following dictionary
#car = {
    "brand": "Ford",
    "model": "Mustang",
    "Max speed" : 150,
    "year" : 1964,
    "Made in": "USA"
}

"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "Max speed" : 150,
    "year" : 1964,
    "Made in": "USA"
}
print(car)
print(car["brand"])



"""
A company wants to save their customers' sign up information in dictionaries , 
you are asked to perform the following task :
create a template dictionary ,with the following keys : first name , last name , e-mail, password.
create a function that accept four argument and return new dictionary for a new customer.
"""
cus_temp = {
'first_name': "" , 'last_name': "" , 'e_mail' : "", 'password':""
}

def createCus(fName, lName, email, password):
    newCus = cus_temp.copy()
    newCus["first_name"] = fName
    newCus["last_name"] = lName
    newCus["e_mail"] = email
    newCus["password"] = password

    return newCus

cus1 = createCus("Henry", "Jones", "h.jones@hgd.com", "asahbavddd")
cus2 = createCus("Bob", "Roggers", "b.roggers@hgd.com", "asdhajs723")

print(cus1)
print(cus2)

"""
 person = {'name': ‘Salam', 'age': 44, 'city': 'Niagara’}
QUESTIONS; Add a key-value named height=164 cm in this dictionary
Delete the key-value named age cm in this dictionary
"""

person = {'name': "Salam", "age": 44, "city": "Niagara"}
print(person)
person["height"] = 164
print(person)

person.pop("age")
print(person)