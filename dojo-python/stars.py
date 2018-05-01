# Part 1
# Create a function called  draw_stars() that takes a list of numbers and prints
# out  *.
# 
# For example:
# 
#     x = [4, 6, 1, 3, 5, 7, 25]
#     draw_stars(x) should print the following in when invoked:
# 
#         **** 
#         ****** 
#         * 
#         *** 
#         ***** 
#         ******* 
#         *************************
# Part 2
# Modify the function above. Allow a list containing integers and strings
# to be passed to the  draw_stars() function. When a string is passed,
# instead of  displaying *, display the first letter of the string
# according to the example below. You may use the .lower() string method
# for this part.
# 
# For example:
# 
#         x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#         draw_stars(x) should print the following in the terminal:
# 
#             **** 
#             ttt 
#             * 
#             mmmmmmm 
#             ***** 
#             ******* 
#             jjjjjjjjjjj


def draw_stars(numbers):
    for element in range(0, len(numbers)):
        if type(numbers[element]) != int:
            insert = numbers[element]
            char = insert[0]
            print("{}".format(char).lower() * len(numbers[element]))
        else:
            print("*" * numbers[element])

x = [4,6,1,3,5,7,25]
y = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
print("Print X")
draw_stars(x)
print("Print Y")
draw_stars(y)
