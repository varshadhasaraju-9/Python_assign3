
def factorial(num):
    """
    :param num: Number for which factorial is calculated
    :return: Factorial of the Number (int)
    """

    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact
    
number = int(input("Enter a number: "))
result = factorial(number)

print(f"Factorial of {number} is:", result)