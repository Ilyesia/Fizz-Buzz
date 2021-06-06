for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    
"""
range is non inclusive this is why we use 101 instead of 100
n variable can be substituted for anything really.
the % modulus always returns a remainder thus we can use the modulus to divided the numbers we parse

Nested if statement alternative
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

String concatenation alternative
for number in range(1, 101):
    string = ""

    if number % 3 == 0:
        string += "Fizz"
    if number % 5 == 0:
        string += "Buzz"
    
    if string == "":
        print(number)
    else:
        print(string)
        
This format checks whether the number is present and adds to the string if 3 is present it add Fizz if 5 is present it adds Buzz to Fizz."""