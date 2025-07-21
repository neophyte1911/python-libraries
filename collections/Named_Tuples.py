# Python code to demonstrate namedtuple()
'''
namedtuple is a factory function for creating tuple subclasses
with named fields.

Provides a readable and convenient way to define simple
classes
'''

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')



'''

ACCESS

'''

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))


'''

CONVERSIONS

'''

# initializing iterable
li = ['Manjeet', '19', '411997']

di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))


'''

Operators

'''

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)

# ._replace returns a new namedtuple, 
# it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Manjeet'))

# Student.__new__ returns a new instance of Student(name,age,DOB)
print(Student.__new__(Student,'Himesh','19','26082003'))


