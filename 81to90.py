print(" 81.	Create a Class Rectangle\n 82.	Class Circle\n 83.	Class BankAccount\n 84.	Class Student\n 85.	Class Car and Inheritance\n 86.	Class ComplexNumber\n 87.	Class Point\n 88.	Classmethod and Staticmethod\n 89.	Property Decorators\n 90.	Class Employee with Inheritance\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 81:
# Define attributes length and width. Include methods to calculate area and perimeter.
    class Rectangle:
        def __init__(self,length,width):
            self.length = length
            self.width = width
        def area(self):
                return self.length * self.width
        def perimeter(self):
            return 2 * (self.length + self.width)
    l=int(input("enter the length : "))
    w=int(input("enter the width : "))
    rectangle = Rectangle(l,w)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

elif question == 82:
# Define a class Circle with attribute radius and methods for area and circumference.
    class Circle:
        def __init__(self,radius):
            self.radius = radius
        def area(self):
            return 3.14 * (self.radius ** 2)
        def circumference(self):
            return 2 * 3.14 * self.radius
          
    r=int(input("enter the radius : "))
    circle = Circle(r)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())

elif question == 83:
# Create a BankAccount class with methods for deposit, withdrawal, and checking balance. Prevent overdraft in withdraw.
    class BankAccount:
        def __init__(self,initial_balance):
            self.balance = initial_balance
        def deposit(self,amount):
            self.balance += amount
            return self.balance
        def withdraw(self,amount):
            if amount > self.balance:
                return "Insufficient balance"
            else:
                self.balance -= amount
                return self.balance
        def check_balance(self):
            return self.balance

    inp=int(input("enter the amount :"))
    account = BankAccount(inp)
    print("Initial balance:", account.check_balance())
    np=int(input("enter the amount to be deposited :"))
    account.deposit(np)
    print("Balance after deposit:", account.check_balance())
    p=int(input("enter the amount to be withdrawn :"))
    account.withdraw(p)
    print("Balance after withdrawal:", account.check_balance())
    pn=input("enter 'c' to check balance :")
    if pn=='c':
        print("Balance:", account.check_balance())
    else:
        print("Invalid input")

elif question == 84:
# A Student class with attributes: name, student_id, and grades (list). Include a method to calculate average grade.
    class Student:
        def __init__(self, name, student_id, grades):
            self.name = name
            self.student_id = student_id
            self.grades = grades
            def average_grade(self):
                return sum(self.grades) / len(self.grades)
            def add_grade(self, grade):
                self.grades.append(grade)
            def remove_grade(self, grade):
                self.grades.remove(grade)
            def print_grades(self):
                print(self.grades)
    inp1=input("enter the student id :")
    inp=input("enter the name :")
    inp2=input("enter the grades :")
    student = Student(inp, inp1, inp2)
    print("Average grade:", student.average_grade())
    s=input("enter the grades to be added : ")
    student.add_grade(s)
    print("Grades after adding a new grade:", student.print_grades())
    s1=input("enter the grades to be removed : ")
    student.remove_grade(s1)
    print("Grades after removing a grade:", student.print_grades())

elif question == 85:       
# Create a base class Car with attributes: make, model, year. Create a derived class ElectricCar with an additional battery_size attribute.
    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
    class ElectricCar(Car):
        def __init__(self, make, model, year, battery_size):
            super().__init__(make, model, year)
            self.battery_size = battery_size

    inp1=input("enter the make :")
    inp=input("enter the model :")
    inp2=input("enter the year :")
    inp3=input("enter the battery size :")
    car = ElectricCar(inp1, inp, inp2, inp3)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Year:", car.year)
    print("Battery size:", car.battery_size)

elif question == 86:     
# Implement a class that represents a complex number with real and imaginary parts. Overload addition and subtraction operators (if you want to practice operator overloading in Python).
# gpt
    class ComplexNumber:
        def __init__(self, real, imaginary):
            self.real = real
            self.imaginary = imaginary
        def __add__(self, other):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        def __sub__(self, other):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    inp1=int(input("enter the real part of first complex number :"))
    inp=int(input("enter the imaginary part of first complex number :"))
    inp2=int(input("enter the real part of second complex number :"))
    inp3=int(input("enter the imaginary part of second complex number :"))
    num1 = ComplexNumber(inp1, inp)
    num2 = ComplexNumber(inp2, inp3)
    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)

elif question == 87: 
# Represent a point in 2D space. Add methods to set coordinates and calculate distance from another Point object.
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def set_coordinates(self, x, y):
            self.x = x
            self.y = y
        def distance(self, other):
            return ((self.x - other.x) ** 2 + (self.y - other.y)** 2) ** 0.5
    inp1=int(input("enter the x coordinate :"))
    inp=int(input("enter the y coordinate :"))
    inp2=int(input("enter the x coordinate of second point :"))
    inp3=int(input("enter the y coordinate of second point :"))
    point1 = Point(inp1, inp)
    point2 = Point(inp2, inp3)
    print("Distance between points:", point1.distance(point2))

elif question == 88: 
# Create a class with a regular instance method, a class method, and a static method. Demonstrate their differences.
    class MyClass:
        def __init__(self, value):
            self.value = value

    # Regular instance method
        def instance_method(self):
            return f'Instance method called, value: {self.value}'

    # Class method
        @classmethod
        def class_method(cls):
            return f'Class method called, class: {cls.__name__}'

    # Static method
        @staticmethod
        def static_method():
            return 'Static method called'


    obj = MyClass(10)
    print(obj.instance_method()) 
    print(MyClass.class_method())
    print(obj.class_method())
    print(MyClass.static_method())  

elif question == 89: 
# Create a class that uses @property to control getting and setting of a private attribute.
    class Person:
        def __init__(self, name):
            self._name = name  # Private attribute (conventionally denoted with a single underscore)

        @property
        def name(self):
            """Getter method for the private attribute _name."""
            return self._name

        @name.setter
        def name(self, value):
            """Setter method for the private attribute _name."""
            if not isinstance(value, str):
                raise ValueError("Name must be a string.")
            self._name = value

        @name.deleter
        def name(self):
            """Deleter method for the private attribute _name."""
            print("Deleting name...")
            del self._name

elif question == 90: 
# Base class Employee (name, ID, salary) and child class Manager (with additional attributes). Override a method in the subclass.
    class Employee:
        def __init__(self, name, employee_id, salary):
            self.name = name
            self.employee_id = employee_id
            self.salary = salary

        def display_info(self):
            """Display employee information."""
            return f"Employee: {self.name}, ID: {self.employee_id}, Salary: {self.salary}"

        def calculate_bonus(self):
            """Calculate a 10% bonus for the employee."""
            return self.salary * 0.10


    class Manager(Employee):
        def __init__(self, name, employee_id, salary, department, team_size):
            super().__init__(name, employee_id, salary)
            self.department = department
            self.team_size = team_size

        def display_info(self):
            """Override the display_info method to include manager-specific details."""
            return f"Manager: {self.name}, ID: {self.employee_id}, Salary: {self.salary}, Department: {self.department}, Team Size: {self.team_size}"

        def calculate_bonus(self):
            """Override the calculate_bonus method to provide a 15% bonus for managers."""
            return self.salary * 0.15
    

    
