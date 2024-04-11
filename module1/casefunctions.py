# Function 1, factorial
def factorial(num):
    try:
        num = int(num)
    except:
        print("Value is invalid for a factorial operation.")
        return

    fact = 1    
    for i in range(1, num+1):
        fact *= i

    return fact


# Function 2, palindrome checker
def is_palindrome(word):
    word = str(word)

    reverse = word[::-1]

    return word == reverse


# Function 3, greeter

greeter = lambda name: f"Hello, {name}"