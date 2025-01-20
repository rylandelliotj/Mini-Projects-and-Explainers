class Dog:
    
    # init method allows us to create attributes of object on instantiation
    # Requires a name to be instantiated
    def __init__(self, name, age):
        self.name = name # 'self' denotes the object itself
        print(name) # Prints 'name' immediately
        self.age = age
        
    # Create Methods
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
        
    def add_one(self, x):
        return x + 1
    
    def bark(self):
        print('woof')
    
    # Change attributes in the init method. This allows us to change data in an object
    def set_age(self, age):
        self.age = age
        
d = Dog('Obi', 4) # Instantiate an object of the class 'Dog' with name 'Obi"
d.bark() # Call method on object 'd' and method 'bark' of class 'Dog'
print(d.add_one(2))
print(d.name) # referene 'self.name' attribute

d2 = Dog('Lucca', 12)
print(d2.get_age())
d2.set_age(13)
print(d2.get_age())

#%% Interacting Classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            # Here, we do not need to add "self" to student because it is not an attribute of this class.
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
        # Note: get_grade() method belongs to the ABOVE class, not this class
        # Better to do the method 'get_grade' incase the 'grade' attribute gets changed
            value += student.get_grade()
        return value / len(self.students)
    
s1 = Student('Elliot', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('John', 18, 100)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
course.get_average_grade()

#%% Inheritance

