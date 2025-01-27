# Bottom-up dynamic programming without recursion
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    FibArray = [0, 1]
    for i in range(2, n):
        FibArray.append(FibArray[i-1] + FibArray[i-2])
    return FibArray

# Driver Program
# n = int(input("Enter the value of n: "))
# print(fibonacci(n))