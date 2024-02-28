# Data Structures
#List

list1 = [7 , 8 , 10, 11]
print(list1)

ip_addresses = ["0.181.18.193", "185.143.205.241", "231.17.1.152", "209.38.162.134",
                "210.127.147.60", "123.253.139.179", "18.189.175.77", "138.195.48.167",
                "212.202.103.190", "222.64.208.64"]
print(ip_addresses)

print("Number of IP Addresses:",len(ip_addresses))
print("Type of ip_addresses: ", type(ip_addresses))

list2 = list((2, 5, 17, "name", "Camila", True, 74.32))
print(list2)

print("IP Address at index 0: ", ip_addresses[0])
print("IP Address at index 2: ", ip_addresses[2])
print("IP Addresses at indexes 2,3,4: ", ip_addresses[2:5]) #[2,5)
print("IP Addresses from the beginning till index 4: ", ip_addresses[:5]) #[0,5)
print("IP Addresses from index 5 to the end: ", ip_addresses[5:]) #[5,9]

print("IP Addresses at index -1 (the last item): ", ip_addresses[-1])
print("IP Addresses from index -4 to -2: ", ip_addresses[-4:-1]) #[-4,-1)

ip_addresses2 = ["100.81.18.93", "85.43.5.222", "231.15.10.159"]
ip_addresses.append("100.80.90.1") # + 1
ip_addresses.insert(2, "200.78.99.11") # + 1

# ip_addresses.append(ip_addresses2) # + 1
# ip_addresses.extend(ip_addresses2) # + 3
ip_addresses += ip_addresses2 # ip_addresses = ip_addresses + ip_addresses2
print(len(ip_addresses))
print(ip_addresses)

ip_addresses.remove("85.43.5.222") #Remove an item by value
ip_addresses.pop(4) #Remove an item by index

# del can be used to remove a varibale including a list.

ip_addresses.sort() #Ascending
ip_addresses.sort(reverse=True) #Descending

print()
print("Ex 2")
""" 
We have a list, which is called fruits. And the fruits has the following values.
		Fruits = [‘Apple’, ‘Banana’, ‘Kiwi’]
We want to the reversed order fruits. But please don’t modify the original list.
Please update the original fruits list in memory.
"""

Fruits = ["Apple","Banana", "Kiwi"]

Fruit2 = Fruits
Fruits2 = Fruits.copy()
print(Fruits)

Fruits2.sort(reverse=True) # Fruits2.reverse()
print(Fruits)
print(Fruits2)
"""
Add new item to list after a specified item. Write a program to add item 7000 after 6000 in the following Python List.
		list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
"""
print()
print()
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(list1)

print(list1[2]);
print(list1[2][2]);

list1[2][2].append(7000)
print()
print(list1)