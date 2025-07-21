# Python code to demonstrate OrderedDict()
'''
OrderedDict is a dictionary subclass that maintains the order of
items based on their insertion.

Useful for preserving order when iterating over dictionary
items.

**Slower than normal dict**

Can be used for LRU
'''



from collections import OrderedDict

print("dict")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, val in d.items():
    print(key, val)

print("ordered dict")
od = OrderedDict()
od['d'] = 4
od['b'] = 2
od['a'] = 1
od['c'] = 3

for key, val in od.items():
    print(key, val)


od.move_to_end('a')         # Move 'a' to end
od.move_to_end('c', last=False)  # Move 'c' to front

print(od)

res = od.popitem(last=True)  # Remove last inserted item

od['e'] = 5 # Insert at last position


# Changing values does not affect order
# Equality checks order!!

# Reversing
d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d2 = OrderedDict(reversed(list(d1.items())))

print(d1 == d2) # False

