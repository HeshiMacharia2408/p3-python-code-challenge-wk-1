def calculate_factiorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
print(f"The factorial of {n} is {calculate_factiorial(n)}")