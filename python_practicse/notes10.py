# To create a deep copy of complex objects in Python, you can use the deepcopy function from the copy module. Here is an example:

import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

# Modifying the copied object
deep_copied[0][0] = 99

print("Original:", original)  # Output: Original: [[1, 2, 3], [4, 5, 6]]
# Output: Deep Copied: [[99, 2, 3], [4, 5, 6]]
print("Deep Copied:", deep_copied)

# A shallow copy creates a new object but does not create copies of the nested objects within the original object. Instead, it inserts references to the same objects into the new object.


original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modifying the copied object
shallow_copied[0][0] = 99

print("Original:", original)  # Output: Original: [[99, 2, 3], [4, 5, 6]]
# Output: Shallow Copied: [[99, 2, 3], [4, 5, 6]]
print("Shallow Copied:", shallow_copied)
