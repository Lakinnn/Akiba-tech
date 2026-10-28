print("==== Memory Management and Garbage Collection ====")
"""
1. How does Python manage objects in memory?
Python creates objects in memory when a program runs. Variables refer to those objects.

For example:
numbers = [10, 20, 30]
Python creates a list object, and numbers refers to it.

2. What is garbage collection?
Garbage collection is part of Python's memory management. It helps clean up objects that are no longer needed.
Python primarily uses reference counting, 
along with a garbage collector that can detect certain groups of objects that refer to each other but are otherwise unreachable.

3. Program using del
"""
print("=== Program using del ===")
numbers = [10, 20, 30]
values = numbers

print("Before deleting:")
print("Numbers:", numbers)
print("Values:", values)

del numbers

print("\nAfter deleting numbers:")
print("Values:", values)

#print("num",numbers) raise an error

"""
The output is: 
Before deleting:
Numbers: [10, 20, 30]
Values: [10, 20, 30]

After deleting numbers:
Values: [10, 20, 30]

Explanation
1. What happens when del is used?

del numbers removes the variable name numbers. It does not necessarily destroy the list object.

2. Does deleting one variable always destroy the object?

No. In our example, values still refers to the list, so the list remains available.

3. What happens when an object is no longer referenced?

When an object becomes unreachable, Python can reclaim its memory. Ordinary objects are often reclaimed through reference counting, while cyclic references may require garbage collection.
"""