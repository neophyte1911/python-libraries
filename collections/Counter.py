# Python code to demonstrate Counter()

'''

Counter is a dictionary subclass for counting hashable objects.
Useful for tallying elements and frequency analysis.

'''


from collections import Counter

# Example list of elements
val = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 2]

# Creating a Counter
ctr = Counter(val)

print(ctr)

print(ctr[1]) # --> 1

print(ctr[2]) # --> 3 

print(ctr[5]) # does not exist --> 0


# Adding new elements
ctr.update([2, 3, 3, 3])

# Checking the 'list'
items = list(ctr.elements())
print(items) # --> [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]


# most common
common = ctr.most_common(2)
print(common) # --> [(3, 6), (2, 4)]


# Decrease count of  elements
ctr.subtract([2, 3, 3, 5])
print(ctr) # non existent -> -1




# Arithmetic operation
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

# Addition
print(ctr1 + ctr2)  
# Subtraction
print(ctr1 - ctr2)  

# Intersection
print(ctr1 & ctr2)  
# Union
print(ctr1 | ctr2)

