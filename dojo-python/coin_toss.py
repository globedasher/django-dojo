# Assignment: Coin Tosses
# MandatoryDeadline: Wednesday of Week 1Difficulty Level: BasicEstimated Time:
#     1-2 hrs
#     You're going to create a program that simulates tossing a coin 5,000 times.
#     Your program should display how many times the head/tail appears.
# 
#     Sample output should be like the following:
# 
#               Starting the program...
# 
#               Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so
#               far and 0 tail(s) so far 
#               Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so
#               far and 0 tail(s) so far 
#               Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so
#               far and 1 tail(s) so far 
#               Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so
#               far and 1 tail(s) so far
#               ........
#               Attempt #5000: Throwing a coin... It's a head! ... Got 2412
#               head(s) so far and 2588 tail(s) so far 
# 
#               Ending the program, thank you!
#               Here are some hints that might help:
# 
#                   1. Use the python random module to generate a random number
# 
#                   import random
#                   random_num = random.random()
#                   # the random function will return a floating point number,
#                   # that is 0.0 <= random_num < 1.0
#                   2. Use the python built-in round function to convert that
#                   floating point number into an integer
# 


import random

def coin_flip():
    tail = 0
    head = 0
    for toss in range(0, 50000):
        random_num = random.random()
        if round(random_num) == 0:
            status = 'heads'
            head = 1 + head
            print( "Attempt #{}: Throwing a coin... "
                    "It's a {}! "
                    "Got {} heads so far and {} tails"""
                    .format(toss + 1, status, head, tail))
        if round(random_num) == 1:
            status = 'tails'
            tail = 1 + tail
            print("Attempt #{}: Throwing a coin... "
                    "It's a {}! "
                    "Got {} tails so far and {} heads"
                    .format(toss + 1, status, tail, head))

coin_flip()
print("Ending the program, thank you.")
