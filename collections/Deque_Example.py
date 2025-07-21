# Python code to demonstrate deque()

'''

deque (double-ended queue) is a list-like container with fast
appends and pops on both ends.
Ideal for implementing queues and stacks.

'''

from collections import deque 
    
dq = deque([10, 20, 30])

print(dq)

# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)  

print(dq)


'''

OPERATIONS

'''

# extend(iterable) === extendright
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable) --> extend on left but puts in reverse
dq.extendleft([0, 5])  
print("After extendleft([0, 5]):", dq)

# remove method
dq.remove(20)
print("After remove(20):", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  

print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)


'''

ACCESSING

'''

# Accessing elements by index
print(dq[0])  
print(dq[-1]) 

# Finding the length of the deque
print(len(dq))

# Counting occurrences of a value
print(dq.count(20))  # Occurrences of 20
print(dq.count(30))  # Occurrences of 30

# Rotating the deque
dq.rotate(2)  # Rotate the deque 2 steps to the right
print(dq)

dq.rotate(-3)  # Rotate the deque 3 steps to the left
print(dq)

# Reversing the deque
dq.reverse()  # Reverse the deque
print(dq)