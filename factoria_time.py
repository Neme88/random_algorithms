# O(N!) - FACTORIAL TIME
# Generating all permutations of a list
from itertools import permutations

def generate_permutations(arr):
    return list(permutations(arr))