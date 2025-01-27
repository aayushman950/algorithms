# Function to generate all Fibonacci numbers till nth number
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
        return []
    elif n == 1:
        return [0]  # Return a list with just the first Fibonacci number
    elif n == 2:
        return [0, 1]  # Return a list with the first two Fibonacci numbers
    else:
        fib_sequence = [0, 1]  # List to store Fibonacci numbers
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence

# Driver Program
n = int(input("Enter the value of n: "))  # User input for nth Fibonacci number
print(Fibonacci(n))