# Insertion Sort
#

# get element and compare to previous element
#   if lower than previous element
#       move previous into current element
#       if next element is 
#     position = element -1
#     move elment to temp
#     while element is less than element@position
#         move element@position to element
#         position -=1

def insertion_sort(sort_list):
    print('Insertion sort')
    for element in range(1, len(sort_list)):
        #print(element)
        temp = sort_list[element]
        position = element
        while temp < sort_list[position - 1] and position > 0:
            sort_list[position] = sort_list[position - 1]
            position -= 1
            #print(str(element) + " element")
            #print(str(position) + " position")
        sort_list[position] = temp
    return sort_list

this_list = [6,2,5,1,8,9,4,0,23,54,76,345,76,2345,654,234]
print(insertion_sort(this_list))
