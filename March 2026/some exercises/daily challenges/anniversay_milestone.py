""" Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	"Paper"
5	"Wood"
10	"Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"
If they haven't reached the first milestone, return "Newlyweds". """

def get_milestone(years):
    if years < 1:
        return 'Newlyweds'
    elif years < 5:
        return 'Paper'
    elif years  < 10:
        return 'Wood'
    elif years < 25:
        return 'Tin'
    elif years < 40:
        return 'Silver'
    elif years < 50:
        return 'Ruby'
    elif years < 60:
        return 'Gold'
    elif years < 70:
        return 'Diamond'                   

    return "Platinum"