# for element of list:
#   if lowest
#       mark for insertion at lowest position
#   else 
#       check next

import datetime

check_list = [34,565,7,5467,1,34,76,456,76,4567,87,345,234,65,7678,678,3456,564,56,4567,678,34,576,57523,4565,79,8734,1234,6,564678,76,456,767865,56775,7865,876,897,98,8756,7564,564,675,4,65,645,54,54,34,43446,7678,9898,98,66576,876,65,6,65,65,534,56675,654,65786,7896,765,765778798,877556465,654,876,654,8765,54,876,634,876,654,7896,54,7896,6576,654,5343,576554,654,654,544354676,876,64,654,43,765,3,54,2,43,45,65,7645,543,8756,876,756,54,65,876,7867,8675,765,654,7856,43,876,554,7,67,6,65,54,5,46,76,87,87,87,8,67,5,7,897,98,989,9,77,67,556,4,54,45,34,3,5,676,87,8745,4,895,056,06,9,5,959,5,95,75,87,6,8967,98,7,98,79,786,765,76,5765,565,7,5467,1,34,76,456,76,4567,87,345,234,65,7678,678,3456,564,56,4567,678,34,576,57523,4565,79,8734,1234,6,564678,76,456,767865,56775,7865,876,897,98,8756,7564,564,675,4,65,645,54,54,34,43446,7678,9898,98,66576,876,65,6,65,65,534,56675,654,65786,7896,765,765778798,877556465,654,876,654,8765,54,876,634,876,654,7896,54,7896,6576,654,5343,576554,654,654,544354676,876,64,654,43,765,3,54,2,43,45,65,7645,543,8756,876,756,54,65,876,7867,8675,765,654,7856,43,876,554,7,67,6,65,54,5,46,76,87,87,87,8,67,5,7,897,98,989,9,77,67,556,4,54,45,34,3,5,676,87,8745,4,895,056,06,9,5,959,5,95,75,87,6,8967,98,7,98,79,786,765,76,5765,565,7,5467,1,34,76,456,76,4567,87,345,234,65,7678,678,3456,564,56,4567,678,34,576,57523,4565,79,8734,1234,6,564678,76,456,767865,56775,7865,876,897,98,8756,7564,564,675,4,65,645,54,54,34,43446,7678,9898,98,66576,876,65,6,65,65,534,56675,654,65786,7896,765,765778798,877556465,654,876,654,8765,54,876,634,876,654,7896,54,789897,98,8756,7564,564,675,4,65,645,54,54,34,43446,7678,9898,98,66576,876,65,6,65,65,534,56675,654,65786,7896,765,765778798,877556465,654,876,654,8765,54,876,634,876,654,7896,54,7896,6576,654,5343,576554,654,654,544354676,876,64,654,43,765,3,54,2,43,45,65,7645,543,8756,876,756,54,65,876,7867,8675,765,654,7856,43,876,554,7,67,6,65,54,5,46,76,87,87,87,8,67,5,7,897,98,989,9,77,67,556,4,54,45,34,3,5,676,87,8745,4,895,056,06,9,5,959,5,95,75,87,6,8967,98,7,98,79,786,765,76,5765,565,7,5467,1,34,76,456,76,4567,87,345,234,65,7678,678,3456,564,56,4567,678,34,576,57523,4565,79,8734,1234,6,564678,76,456,767865,56775,7865,876,897,98,8756,7564,564,675,4,65,645,54,54,34,43446,7678,9898,98,66576,876,65,6,65,65,534,56675,654,65786,7896,765,765778798,877556465,654,876,654,8765,54,876,634,876,654,7896,54,7896,6576,654,5343,576554,654,654,544354676,876,64,654,43,765,3,54,2,43,45,65,7645,543,8756,876,756,54,65,876,7867,8675,765,654,7856,43,876,554,7,67,6,65,54,5,46,76,87,87,87,8,67,5,7,897,98,989,9,77,67,556,4,54,45,34,3,5,676,87,8745,4,895,056,06,9,5,959,5,95,75,87,6,8967,98,7,98,79,786,765,76,5765]

# The following is used to calculate running time.
begin = datetime.datetime.now()

# The following variable is used to hold the starting position of the list
# check.
start = 0
length = len(check_list)
while start < length / 2:
    # Get a starting value to compare for min and max
    max_temp = check_list[start]
    min_temp = check_list[start]
    # Iterated through the length of the list
    for element in range(start,length - start):
        # If the value of a list element is less than the current minimum,
        # change the minimum value and create an index for the minimum value of
        # the list.
        if check_list[element] < min_temp:
            min_temp = check_list[element]
            min_position =  element
        # If the value of a list element is less than the current maximum,
        # change the maximum value and create an index for the maximum value of
        # the list.
        if check_list[element] > max_temp:
            max_temp = check_list[element]
            max_position =  element
    check_list[min_position] = check_list[start]
    check_list[start] = min_temp
    check_list[max_position] = check_list[length - 1 - start]
    check_list[length - 1 - start] = max_temp
    start += 1
    
# The following is used to calculate running time.
end = datetime.datetime.now()
print(check_list)
delta = end - begin
print("It only took " + str(delta) + " < (seconds) to complete the sort")

# According to data from the times, just iterating through the list once and
# doing a bubble sort is faster than doing a min max sort and going through
# half the array...
# 
# Just sorting with the min function took 0.038911 seconds
# Changing the function reduced the operating time to 0.030363 seconds
