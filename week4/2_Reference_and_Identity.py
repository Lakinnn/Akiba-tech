print("==== Reference and Object Identity ====")
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)

"""
1. The output is :
True
False
True 

2. Difference between 'is' and '==': 
is —> Identity

Checks whether two variables refer to the exact same object in memory.

== —> Equality

Checks whether two objects have equal values.

3. Why do a and c have different identities?
These two statements create different situations:
b = a
c = [10, 20, 30]

The first statement creates another reference to the existing list.

The second statement creates a new list containing the same values.

Two objects can have equal values but different identities.
"""