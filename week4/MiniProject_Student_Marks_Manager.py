
print("=" * 5, "STUDENT MARKS MANAGER", "=" * 5)

# Original list
marks = [75, 80, 65, 90, 85]

# Shared reference
shared_marks = marks

# Independent copy
copied_marks = marks.copy()

# Modify only the copied list
copied_marks.append(95)

# Display the lists
print("Original marks:", marks)
print("Shared reference:", shared_marks)
print("Copied marks:", copied_marks)

# Compare identity and equality
print("\nOriginal and shared reference are identical:", marks is shared_marks)

print("Original and copied lists have equal values:", marks == copied_marks)

print("Original and copied lists are identical:", marks is copied_marks)
