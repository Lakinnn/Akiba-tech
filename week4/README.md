## Project Reflection

### 1. Why does modifying a shared reference affect the original list?

A shared reference means that two variables refer to the same list object. When one variable modifies the list, the change is visible through the other variable because both refer to the same object.

### 2. Why does modifying the copied list not affect the original list?

The `copy()` method creates a separate list object. Therefore, adding or removing elements from the copied list does not change the original list.

### 3. What is the difference between equality and identity in Python?

Equality, checked using `==`, compares the values of two objects. Identity, checked using `is`, checks whether two variables refer to the exact same object. Two lists can contain equal values while having different identities.