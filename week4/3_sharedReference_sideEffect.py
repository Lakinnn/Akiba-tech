numbers = [1, 2, 3]
values = numbers

values.append(4)

print("==== With .append() ====")
print("Numbers",numbers)
print("Values",values)

"""
1. The output:
[1, 2, 3, 4]
[1, 2, 3, 4]

2. Why does modifying values affect numbers?
Because both variables refer to the same list.

(values = numbers) does not create a new list. 
It creates another reference to the existing list.

Therefore, when we use:
values.append(4)

We modify the shared list, and both variables show the change.

3. Rewrite the code to avoid changing the original list
We can use the { list's copy() }method.
"""
numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print("\n","==== With .copy() ====")
print("Numbers:", numbers)
print("Values:", values)


"""Output:
Numbers: [1, 2, 3]
Values: [1, 2, 3, 4]

Now numbers and values refer to separate lists.
"""