import datetime

""" 
we will learn basics about creating and Instantiating classes
we will learn about Inheritance, class and Instance variables , class methods and static methods.
data and functions associated with specific class those are called attributes and methods
and you hear a lot about them in pythonic course 
"""


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
    '''
    when we create methods within a class they receive the instance as their first argument
    by convention it is called self
    '''

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount # or self.raise_amount if required at instance level
        # if it is not accessed like  Employee.raise_amount or self.amount it will give error

    @classmethod
    def set_raise_amt(cls, amount): # just like reg methods we used self , here we use cls
        cls.raise_amount = amount

    # class methods can be used as alternative contructor
    # Example the data that we get in a concatenated firstname , lastname , salary a
    # Now this string ca be split to individual argument and return an instance of the class

    @classmethod   # Here we are using it as alternative constructor as it's returning an instance
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # above we don't want to parse this string everytime Instead lets create alternate constructor
    # real world example of alternative constructor is datetime.py

    '''
    now that we have looked at cls methods 
    let's look at static methods
    1. Instance/regular methods take  self af first method 
    2. Class methods take cls as first parameter
    3. Static method take no argument, 
    
    Static methods just behave like regular functions but have some kind of logical
    connection to the class so they are part of the class definition
    '''

    @staticmethod
    def is_workday(day):  # they don't take instance (self) / class (cls) as first argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# By simply inheriting the parent class child class has inherited all the parent functionality


class Developer(Employee): # put class name  we want to inherit in the brackets
    raise_amount = 1.10
    # now if we want to add extra attribute say "prog language" for the child class we can write the below code

    ''' 
    def __init__(self, first, last, pay, prog_lang):
            self.first = first  # this is equal to emp1.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com'
            self.prog_lang = prog_lang 
    ''' # or
    def __init__(self,first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # in order to handle the employee first , last and pay
        # Employee.__init__(self, first, last, pay)
        ''' both invoke super method and let that super class handle its attributes '''
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("---> ",emp.fullname())
# even without any declaration the Developer class will have all the attributes of the parent class


emp_1 = Employee('Corey','Schafer',50000) # we can leave out self adn just pass the fields
emp_2 = Employee('Test','User', 60000)

my_date = datetime.date(2017,7,11)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test','Employee',600000,'Java')

# print(help(Developer))
print("Is it a weekday : ", Employee.is_workday(my_date))

print("dev_1 is : ",dev_1.first)
print("dev_1 is : ",dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.add_employee("mary jane")

print(mgr_1.pay)

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
# observe the above print result
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

'''Now we will be learning Class methods , Static methods, Regular methods
   Regular methods take self / instance as the first parameter
   how to make methods that takle class as first argument ? 
   now to do that we are going to use decorator called class method 
   @classmethod ''' # implementation line 72


# class methods can be used as alternative contructor
# Example the data that we get in a concatenated firstname , lastname , salary a
# Now this string ca be split to individual argument and return an instance of the class

employee_1 = "John-Doe-70000"
employee_2 = "Steve-Smith-50000"
employee_3 = "Jane-Doe-90000"

first, last, pay = employee_1.split("-")
new_emp_1 = Employee(first,last,pay) # then creating an object, not the best way so refer to cls method


# Python provides 2 main built in methods

print("Manager is subclass of Developer - (T/F) : ", issubclass(Manager, Developer))
print("mgr_1 is an Instance of Manager  - (T/F) : ",isinstance(mgr_1, Manager))
























