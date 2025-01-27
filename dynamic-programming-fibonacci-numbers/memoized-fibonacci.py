# Memoization approach for Fibonacci
FibArray = {0: 0, 1: 1}  # Initialize base cases in a dictionary

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return []
    if n in FibArray:
        return FibArray[n]  # Return the memoized value if it's already computed
    else:
        # Recursively compute the Fibonacci number, memoize it, and return
        FibArray[n] = fibonacci(n-1) + fibonacci(n-2)
        return FibArray[n]

def fibonacci_up_to_n(n):
    if n < 0:
        print("Incorrect input")
        return []
    result = []
    for i in range(n):
        result.append(fibonacci(i))
    return result

# Driver Program
n = int(input("Enter the value of n: "))  # User input for nth Fibonacci number
print(fibonacci_up_to_n(n))