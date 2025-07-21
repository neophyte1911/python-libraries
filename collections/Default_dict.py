# Python code to demonstrate defaultdict()

'''

defaultdict is a dictionary subclass that provides a default
value for missing keys.
Simplifies code that involves dictionary lookups with default
values

'''

from collections import defaultdict

d = defaultdict(list) #default value is an empty list

d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)

print(d['juices'])

# int -> def value 0
# list -> def value []
# str -> def value ""


d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])