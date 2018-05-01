# Output to be:
# Number is 1. This is an odd number.
# Number is 2. This is an even number.
# Number is 3. This is an odd number.
# ...
# Number is 2000 This is an even number.

for number in range(1, 2000):
    if number % 2 == 1:
        print("Number is {}. This is an {} number.".format(number, "odd"))
    elif number % 2 == 0:
        print("Number is {}. This is an {} number.".format(number, "even"))
