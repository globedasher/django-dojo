# Assignment: Names
# MandatoryDeadline: Thursday of Week 1Difficulty Level: BasicEstimated Time: 1-2 hrs
# Part I
# 
# Given the following list:
# 
# students = [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# Create a program that outputs:
# 
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
#
# Part II
# 
# Now, given the following dictionary:
# 
# users = {
#  'Students': [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }
# Create a program that prints  the following format (including number of characters in each combined name):
# 
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13


students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
 ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
 ]
}

# Part I
print("Part I")
for item in students:
    print item['first_name'], item['last_name']

# Part II
# users is a dicationary with two items: 'Students' and 'Instructors'
# These are dictionary items with lists full of dictionary items
print('\n')
print("Part II")
for person_list in users:
    print(person_list)
    for item in enumerate(users[person_list]):
        print str(item[0] + 1) + ' - ' + item[1]['first_name'].upper(), \
            item[1]['last_name'].upper() + ' - ' + \
            str((len(item[1]['first_name'])+len(item[1]['last_name'])))
    print('\n')
