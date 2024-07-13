# Script to list prime numbers within a range of number
# the strategy is toe define a divisor

for number in range(2, 20):
    # define divisor
    for divisor in range(2, number):
        # set the condition for division 
        if number % divisor == 0:
            print(number, 'Equals', divisor, '* ', number//divisor)
            break
    else:
        print(number, "is a primer number")


