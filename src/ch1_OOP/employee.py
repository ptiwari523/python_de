class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first_name= first
        self.last_name = last

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

emp1 = Employee("Punit", "Tiwari")
emp1.fullname = "Ankit Sharma"
print(emp1.first_name)
print(emp1.last_name)
print(emp1.fullname)
print(emp1.email)