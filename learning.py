def method_name():
    print("A method")

class Person:
    def __init__(self, name, dob, height):
        self.name = name
        self.date_of_birth = dob
        self.height = height

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if (self.__has_number(new_name)):
            print("sorry person name cant have number")

        self.name = new_name
    def __has_number(self, string):
        return "0" in string 
    
    def get_summary(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"
        
a_person = Person("Mostafa", "1990-09-19", "5feet 4 inches")
b_person = Person("Robot", "2023-01-01", "6 feet")

method_name()
print(a_person.get_summary())
print(b_person.get_summary())

a_person.set_name("Mostafa Al Mamun Fahim")
print(a_person.get_summary())

print(a_person.date_of_birth)

a_person.set_name("0Fahim")
a_person.name = "0Fahim"
print(a_person.name)