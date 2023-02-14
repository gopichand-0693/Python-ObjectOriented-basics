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

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # Special init method , another language it is called constructor
        self.first = first  # this is equal to emp1.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.num_of_emps += 1


    def fullname(self): # takes object (self) is taken as first argument by default
        return 'Employee full name : {} {}'.format(self.first, self.last)
        # 'Employee full name : {} {}'.format(emp_1.first, emp_1.last) we have replaced emp1_1 with self


    '''
    Lets replace the below code and pull out 1.05 as it is being accessed by all the class instances 
    and make it class variable   
      def apply_raise(self):
            self.pay = self.pay * 1.04
    '''

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount # or self.raise_amount if required at instance level
        # if it is not accessed like  Employee.raise_amount or self.amount it will give error




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


# class variables are variables that are shared among all instances
'''
while instance variables can can be unique 
clas variables should be same for it to be referred for all the objects
Imagine what kind of data would be shared among the instances in Employee scenario
'''
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

''' all the above 3 ways of accessing class variable are valid but in a hierarchy for obj
it means for the emp_1.raise_amount looks for the raise_amount 
in it's attributes or any class it inherits from if not it will refer to class attribute'''

# to get more clarity lets print out name space of emp_1

print(emp_1.__dict__)  # printing the name space of emp_1
# result  {'first': 'Corey', 'last': 'Schafer', 'pay': 52000.0, 'email': 'Corey.Schafer@company.com'}

print(Employee.__dict__)
# result
'''
{'__module__': '__main__',  ####### 'raise_amount': 1.04, #####
 '__init__': <function Employee.__init__ at 0x00000185169EB550>, 
 'fullname': <function Employee.fullname at 0x0000018516D01E50>, 
 'apply_raise': <function Employee.apply_raise at 0x0000018516D01DC0>, 
 '__dict__': <attribute '__dict__' of 'Employee' objects>, 
 '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
'''

# raise_amount is only present in namespace of class but not the individual instance namespaces

print(Employee.num_of_emps)


# Now that we have class variables doe we have class methods ? - short ans Yes















