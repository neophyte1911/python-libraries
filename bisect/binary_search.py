'''

bisect module provides support for maintaining sorted lists
using binary search.
Functions bisect_left and bisect_right help in finding insertion
points for elements in sorted lists.

'''

from bisect import bisect_left, bisect, bisect_right

from bisect import insort_left, isort, insort_right


#Find insertion indices for the value 4 in a sorted list using different bisect functions.

li = [1, 3, 4, 4, 4, 6, 7] 

print(bisect(li, 4)) # right --> 5
print(bisect.bisect_left(li, 4)) # left --> 2
print(bisect.bisect_right(li, 4, 0, 4)) #  also right (sorted list, value, start index, end index ) --> 4


#Insert the value 5 into a sorted list while keeping it sorted, using different insertion strategies.
l1 = [1, 3, 4, 4, 4, 6, 7]  
l2 = [1, 3, 4, 4, 4, 6, 7]  
l3 = [1, 3, 4, 4, 4, 6, 7]  


bisect.insort(l1, 5)
print(l1) 

bisect.insort_left(l2, 5) # left
print(l2)

bisect.insort_right(l3, 5, 0, 4) # also right (sorted list, value, start index, end index )
print(l3)


'''

Implementing binary sort

'''
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

a  = [1, 2, 4, 4, 8]
x = 4
res = BinarySearch(a, x)

if res == -1:
    print(f"{x} is not present")
else:
    print(f"{x} is present at index {res}")


'''

Implementing 'Finding value smaller than x'

'''

def valueSmallerThanX(a, x):
    i = bisect_left(a, x)
    if i:
        return (i-1)
    else:
        return -1

a  = [1, 2, 4, 4, 8]
x = 7
res = valueSmallerThanX(a, x)

if res == -1:
    print(f"{x} is smallest")
else:
    print(f"{res} is smallest")

