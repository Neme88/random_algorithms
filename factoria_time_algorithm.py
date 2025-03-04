# O(N!) - FACTORIAL TIME
# Generating all permutations of a list
from itertools import permutations

def generate_permutations(arr):
    return list(permutations(arr))

# Example Usage
if __name__ == "__main__":
     # Test O(N!)
    print(generate_permutations([1, 2, 3]))  # Output: List of all permutations
