# O(2^N) - EXPONENTIAL TIME
# Recursive Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
     # Test O(2^N)
    print(fibonacci(10))  # Output: 55