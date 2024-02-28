class MyClass:
    x = 0
    y = 0

myObj1 = MyClass()
print("myObj1", str(myObj1.x), " | " , str(myObj1.y))

myObj2 = MyClass()
myObj2.x = 10
myObj2.y = 20

print("myObj1", str(myObj1.x), " | " , str(myObj1.y))
print("myObj2", str(myObj2.x), " | " , str(myObj2.y))

class Chair:
    type = ""
    color = ""
    height = 0
    number_of_legs = 0

chair1 = Chair()
chair1.type = "A"
chair1.color = "Black"
chair1.height = 36
chair1.number_of_legs = 4

chair2 = Chair()
chair2.type = "B"
chair2.color = "White"
chair2.height = 50
chair2.number_of_legs = 1

print()
print("CHAIRS")
print(chair1)
print(chair2)
print("Chair 1:", chair1.type, " | ", chair1.color, " | ", str(chair1.height), " | ", str(chair1.number_of_legs))
print("Chair 2:", chair2.type, " | ", chair2.color, " | ", str(chair2.height), " | ", str(chair2.number_of_legs))

class Profession:
    title = ""
    median_salary = 0
    qualifications = ""

doctor = Profession()
doctor.title = "Doctor"
doctor.median_salary = 120000
doctor.qualifications = "MD, MBBS"


class DChair:
    type = ""
    color = ""
    height = 0
    number_of_legs = 0

    def __init__(self, chair_type, chair_color, chair_height, chair_number_of_legs):
        self.type = chair_type
        self.color = chair_color
        self.height = chair_height
        self.number_of_legs = chair_number_of_legs

    def __str__(self):
        return self.type+ " | "+ self.color+ " | "+ str(self.height)+ " | "+ str(self.number_of_legs)

    def paint_chair(self, new_color):
        self.color = new_color
        print("The chair has been painted in ", new_color)

dChair1 = DChair("C", "White",40,4)
dChair2 = DChair("D","Black",60,4)

print()
print("DChair 1:", dChair1.type, " | ", dChair1.color, " | ", str(dChair1.height), " | ", str(dChair1.number_of_legs))
print("DChair 2:", dChair2.type, " | ", dChair2.color, " | ", str(dChair2.height), " | ", str(dChair2.number_of_legs))
print()
print(dChair1)
print(dChair2)

print()
dChair1.paint_chair("Blue")
print(dChair1)

"""
del dChair1
print(dChair1)
"""

##########EX.1 DOCUMENT###############
class FTPDocument:
    title = ""
    type = ""
    size = 0
    extension = ""
    folder_path = ""

    def __init__(self, doc_title, doc_type, doc_size, doct_ext, path):
        self.title = doc_title
        self.type = doc_type
        self.size = doc_size
        self.extension = doct_ext
        self.folder_path = path

    def __str__(self):
        return "DOCUMENT: " + self.folder_path + "\\" + self.title + "." + self.extension

    def printDoc(self):
        print("Document was sent to the printer")

    def emailDoc(self, email_to):
        print("Document was emailed to:", email_to)

print()
print("FTP DOCUMENTS")
doc1 = FTPDocument("camila", "doc", 100.00, "doc", "\\WEB\\ROOT")
doc2 = FTPDocument("clement", "xls", 150.00, "xls", "\\WEB\\ROOT")

doc1.printDoc()
doc2.emailDoc("han.kate@gamil.com")
print(doc1)
print(doc2)

# Empty Class
class MySuperClass:
    pass

