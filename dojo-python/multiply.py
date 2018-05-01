#Create a function called 'multiply' that reads each value in the list (e.g. a =
#        [2, 4, 10, 16]) and returns a list where each value has been multiplied
#by 5.
#
#The function should multiply each value in the list by the second argument. For
#example, let's say: 
#
#    a = [2,4,10,16] 
#    Then:
#    b = multiply(a, 5) 
#    print b
#
#    Should print [10, 20, 50, 80 ].

def multiply(element_list):
    for element in range(0, len(element_list)):
        element_list[element] = element_list[element] * 5

a = [2,4,10,16]
multiply(a)
print(a)
