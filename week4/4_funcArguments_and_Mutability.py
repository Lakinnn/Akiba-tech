print("==== Function Arguments and Mutability ====")

def update_list(items):
	items.append(100)

print("\n","=== With items.append inside function ===")
scores = [50, 60, 70]
update_list(scores)

print("Scores: ",scores)

"""
1. The output is: [50, 60, 70, 100]
2. Why the original list changes after the function call?

* Because inside the function, items.append(100) modifies the list directly. 


3. Modify the function so that it creates and returns a new list without changing the original list.
"""
def update_list(items):
    new_list = items.copy()
    new_list.append(100)
    return new_list

scores = [50, 60, 70]
updated_scores = update_list(scores)

print("\n","=== With items.copy() inside function ===")
print("Original:", scores)
print("Updated:", updated_scores)

"""
Explanation:
1. items.copy() creates a separate list.
2. new_list.append(100) modifies the new list.
3. return new_list sends the new list back to the caller.
4. The original scores list remains unchanged. """