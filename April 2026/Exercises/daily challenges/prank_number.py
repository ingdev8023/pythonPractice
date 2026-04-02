"""Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10]."""


def fix_prank_number(arr):
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    print(diffs)
    expected_diff = max(set(diffs), key=diffs.count)
    print(expected_diff)

    for i in range(len(diffs)):
        if diffs[i] != expected_diff:
            print(diffs[i])
            # Step 4: fix the wrong number
            arr[i+1] = arr[i] + expected_diff
            break

    return arr
    
print(fix_prank_number([2, 4, 7, 8, 10]))
print(fix_prank_number([10, 10, 8, 7, 6]))
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
print(fix_prank_number([4, 1, -2, -5, -8, -5]))
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
print(fix_prank_number([-5, 5, 10, 15, 20]))