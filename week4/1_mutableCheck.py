print("==== Mutable Immutable Check ====")

"""
Explanation:
Mutable objects: Objects that can be changed after they are created. 
Examples: lists, sets and dictionaries.
Immutable objects: Objects that cannot be changed after they are created. 
Examples: strings, integers, and tuples."""


# Modifying a list (mutable)
nums= [10,20,30]
numbers = [10, 20, 30]
numbers[0] = 40

print("\n","-"*20,"\n","Mutable\n","-"*20)
print("Old list: ", nums)
print("New list:", numbers)

# Modifying a string (immutable)
words = "Hello"
word = words + " World"

print("\n","-"*20,"\n","Immutable\n","-"*20)
print("Old string: ", words)
print("New string:", word)

"""The list is mutable, 
so we can change its first element from 10 to 40 
without creating a new list.

The string is immutable, 
so we cannot change its existing characters.
Instead, word + " World" creates a new string, 
which we assign to word. """