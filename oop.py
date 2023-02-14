# we will learn basics about creating and Instantiating classes
# we will learn about Inheritance,
# class and Instance variables , class methods and static methods.

# data and functions associated with specific class
# those are called attributes and methods
# and you hear a lot about them in pythonic course

class Employee:
    pass

# class is a blueprint for creating instances of real world or abstract objects
# we add the features as attributes and functionality as methods.


emp1 = Employee
emp2 = Employee

print("Emp1 is : " + str(emp1) +" \nEmp2 is : "  + str(emp2))

print(emp1 == emp2) # true

# emp1 and emp2 are called instance variables and the data that contained in them is unique to them

# lets emp1 wanted to have fname and lname

emp1.first = "Corey"
emp1.last = "Schafer"
emp1.email = 'corey.scahfer@company.com'
emp1.pay = 50000

emp2.first = "Test"
emp2.last = "User"
emp2.email = 'Test.User@company.com'
emp2.pay = 60000

print(emp1.email)
print(emp2.first)

# Instead of manually creating vars each time we will create a blueprint for these vars

class Employee:

    def __init__(self, first, last, pay):  #pecial init method , another language it is called constructor
        self.first = first  # this is equall to emp1.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self): # takes object (self) is taken as first argument by default
        return 'Employee full name : {} {}'.format(self.first, self.last)
        # 'Employee full name : {} {}'.format(emp_1.first, emp_1.last) we have replaced emp1_1 with self


'''
when we create methods within a class they receive the instance as their first argument
by convention it is called self
'''

emp_1 = Employee('Corey','Schafer',50000) # we can leave out self adn just pass the fields
emp_2 = Employee('Test','User', 60000)


'''
ny the above code below code can be deleted reduced 
emp2.first = "Test"
emp2.last = "User"
emp2.email = 'Test.User@company.com'
emp2.pay = 60000
'''

print('Employee full name : {} {}'.format(emp_1.first, emp_1.last))
# Instead of preparing full name everytime, lets put this as functionality in one place
# inside the class with proper method definition which also helps in code reuse
# DRY principle

print(emp_1.fullname())

# we can also run the method with the class name itself which makes it bit obvious

print(Employee.fullname(emp_1)) # In such Scenario, we need to manually pass in the obj name (self)

'''
when we run print(emp_1.fullname()) in the background 
print(Employee.fullname(emp_1)) is what actually gets transformed and called out 
'''











