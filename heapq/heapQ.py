'''

Priority Queues:
heapq provides an implementation of the heap queue
algorithm, also known as the priority queue algorithm.

Supports efficient insertion, deletion, and retrieval of the
smallest element.
'''

import heapq

# Creating a list
li = [10, 20, 15, 30, 40]

# Convert the list into a heap
heapq.heapify(li)

print("Heap queue:", li)


'''

Key operations of a heap:

    Push (heappush): Adds an element to the heap while maintaining the heap property.
    Pop (heappop): Removes and returns the smallest element in the heap, again maintaining the heap property.
    Peek: View the smallest element without removing it.
    Heapify: Convert a regular list into a valid heap in-place.

'''

# Appending an element
heapq.heappush(li, 5)

print(li)

# Pop the smallest element from the heap
min_el = heapq.heappop(li)

print("Smallest:", min_el)
print(li)


# Push a new element (5) and pop the smallest element at the same time
min_el = heapq.heappushpop(li, 5)
print("Smallest:", min_el)
print(li)


# Find the 3 largest elements
maxi = heapq.nlargest(3, li)
print("3 largest elements:", maxi)

# Find the 3 smallest elements
mini = heapq.nsmallest(3, li)
print("3 smallest elements:", mini)



# Replacing the smallest element (10) with 5
min_el = heapq.heapreplace(li, 5)

print(min_el)
print(li)

# Merging Heaps
h2 = [2, 4, 6, 8]

# Merging the lists
li = list(heapq.merge(li, h2))
print("Merged heap:", li)

'''
+ fast, efficient and space efficient
+ Can use to implement priority queue, heaps, binary trees
- limited functionality, no sorting, no random access
- not thread safe
'''

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


sorted_list = heapsort([3, 1, 4, 1, 5, 9])
print(sorted_list)