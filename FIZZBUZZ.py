Limit = 1000
number = 1

while number <= Limit: 
    
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    
    number = number + 1