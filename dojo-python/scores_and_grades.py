# Create a program that prompts the user ten times for a test score between 60
# and 100. Each time a score is generated, your program should display what is
# the grade of that score. Here is the grade table:
# 
#     Score: 60 - 69; Grade - D
#     Score: 70 - 79; Grade - C
#     Score: 80 - 89; Grade - B
#     Score: 90 - 100; Grade - A
#     The result should be like this...
# 
#     Scores and Grades
#     Score: 87; Your grade is B
#     Score: 67; Your grade is D
#     Score: 95; Your grade is A
#     Score: 100; Your grade is A
#     Score: 75; Your grade is C
#     Score: 90; Your grade is A
#     Score: 89; Your grade is B
#     Score: 72; Your grade is C
#     Score: 60; Your grade is D
#     Score: 98; Your grade is A
#     End of the program. Bye!


# I wrote this asuming the end user would only enter integers inside the ranges
# specified.
def scores_and_grades(gradelist):
    #print(gradelist)
    for grade in range(0, len(gradelist)):
        #print(gradelist)
        if gradelist[grade] > 90:
            print("Score: {}; Your grade is A!".format(gradelist[grade]))
        elif gradelist[grade] < 89 and gradelist[grade] > 80:
            print("Score: {}; Your grade is B!".format(gradelist[grade]))
        elif gradelist[grade] < 79 and gradelist[grade] > 70:
            print("Score: {}; Your grade is C!".format(gradelist[grade]))
        else:
            print("Score: {}; Your grade is D!".format(gradelist[grade]))

def enter_scores():
    scores = []
    for num in range(0, 10):
        scores.append(input("Enter the student's score (between 60 and 100):"))
    return scores

def main():
    values = enter_scores()
    scores_and_grades(values)
    print("End of the program. Bye!")

main()
