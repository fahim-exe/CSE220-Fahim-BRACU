def method_name():
    print("A method")

class Person:
    def __init__(self, person_name:str, year_of_birth:int, ht_inches:int=None):
        self.name = person_name
        self.date_of_birth = year_of_birth
        self.height = ht_inches
         
    def get_year_of_birth(self):
      return self.date_of_birth

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if (self.__has_number(new_name)):
            print("sorry person name cant have number")

        self.name = new_name
    def __has_number(self, string):
        return "0" in string 
    
    def get_summary(self):
        pass
        #return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height if self.height is not None else 'Not given'}"

person_list = [Person("Mostafa", 2002, 72),
               Person("Al Mamun ", 1980, 100),
               Person("Fahim", 1996),
               Person("Alucard", 1999, 89),
               Person("Chengsi", 1971, 86)]

#for person in person_list:
#if person.get_year_of_birth() is not None and person.get_year_of_birth() >=1990:
#print(person.get_summary())


class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, student_id: str):
        super().__init__(person_name, year_of_birth)
        
        self.sid = student_id
        self.email = email_id

    def get_summary(self):
        
        return f"Name:{self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()}"


    def __str__(self) -> str:
        pass
        #return self.get_summary()
    #def __repr__(self) -> str:
       #return self.get_summary()

#student = Student("Mostafa Al Mamun Fahim", 1970, "hellofahim@gmail.com", "20101214")
#print(student)
#student.set_name("Mostafa")
#print(student)


class Teacher(Person):
    def __init__(self, person_name: str, year_of_birth: int, department:str):
        super().__init__(person_name, year_of_birth)
        self.dept = department

    def get_summary(self):
        return f"{self.get_name()} is a Teacher"

new_person_list = [
    Person("Mostafa", 1990),
    Student("S", 2000, "s@gmail.com", "stid"),
    Teacher("T", 1980, "tid")
]


for p in new_person_list:
    print(p.get_summary())
    


