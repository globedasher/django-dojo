# Bubble sort
# Iterate through array
# Swap element with the element above if it is larger
# Move to the next element

import datetime

def swap(swap_list):
    # This function will swap the elements in the list and is called from the
    # main function.
    temp = swap_list[0]
    swap_list[0] = swap_list[1]
    swap_list[1] = temp
    return swap_list

def main(sort_this):
    # I am going to assume the list will always be unsorted.
    unsorted = 0
    while unsorted < len(sort_this):
        unsorted += 1
        # With each iteration of the following for loop, the largest number
        # will be placed at the end of the list. Therefore, the range of the
        # for loop can decrease by one each loop. Once the loop reaches zero
        for element in range(len(sort_this) - 1):
            # if an element is larger than the element afer it, send the two
            # elements to the swap function.
            if sort_this[element] > sort_this[element + 1]:
                swap_these = [sort_this[element], sort_this[element + 1]]
                sort_this[element], sort_this[element + 1] = swap(swap_these)
    return sort_this

list_to_sort = [34,6,456,245,675,367,76,4567,34567,8785,3456,675,356,76557,347637,567643,7657,6756756,4767,56756,5764677,98734,27834,45,667,3456,87,5678,567,678,678,678,5678,3456,68,5678567,987,876,7685,98,865,98,786,908,987,9865,76,876,65,76,987,98,567,98,877676,65,78687,987,98,-89,78667565,987,656554,8756,654676,987,65,765,654,76,7645,654,4376,987,765,654,43,65,54,43,3,356474,43545,654,65,54,876,6534,543,8756,3984,498,5654,567,67,8,7,456,8,78,5,6,87,6,6756,34,5645,567,98,876,908754,756,45,8967675,987,765,987,675,5,3,6,3,9,2,1,0]
start = datetime.datetime.now()
print(main(list_to_sort))
stop = datetime.datetime.now()
delta = stop - start
print("It only took " + str(delta) + " < (microseconds) to complete the sort")
