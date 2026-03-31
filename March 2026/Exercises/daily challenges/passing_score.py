""" Passing Exam Count
Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam. """

def passing_count(scores, passing_score):
    return len([score for score in scores if score >= passing_score])

print(passing_count([90, 85, 75, 60, 50], 70))     
print(passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75))     