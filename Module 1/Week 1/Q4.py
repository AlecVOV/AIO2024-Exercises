import math

#Calculate factorial of a number:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#Calculate sin function:
def approx_sin(x, n):
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2*i + 1) / factorial(2*i + 1)
        result += term
    return result

#Calculate cos function:
def approx_cos(x, n):
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2*i) / factorial(2*i)
        result += term
    return result

#Calculate sinh function:
def approx_sinh(x, n):
    result = 0
    for i in range(n):
        term = x**(2*i + 1) / factorial(2*i + 1)
        result += term
    return result

#Calculate cosh function:
def approx_cosh(x, n):
    result = 0
    for i in range(n):
        term = x**(2*i) / factorial(2*i)
        result += term
    return result

def main():
    # Enter x and n from user
    x = float(input("Enter x (radian): "))
    n = int(input("Enter n (repeated time): "))

    while n <= 0:
        print("n have to a positive number. Please enter again")
        n = int(input("Re-enter (n): "))

    # Calculate and print result
    print(f" sin({x}): {approx_sin(x, n):.8f}")
    print(f" cos({x}): {approx_cos(x, n):.8f}")
    print(f" sinh({x}): {approx_sinh(x, n):.8f}")
    print(f" cosh({x}): {approx_cosh(x, n):.8f}")


main()