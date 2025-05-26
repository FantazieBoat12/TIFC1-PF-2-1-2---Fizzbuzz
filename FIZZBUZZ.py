Limit = 1000
number = 1

while number <= Limit: 
    
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 15 == 0:
        print("FIZZBUZZ")
    else:
        print(number)
    
    number = number + 1