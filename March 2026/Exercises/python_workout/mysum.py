def mysum(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
print(mysum(1,2,4,56,7))

def mysum_versioned(numbers, start):
    sum = start
    for i in numbers:
        sum += i
    return sum

print(mysum_versioned([1,2,4,56,7], 6))

def myavg(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

print(myavg(1,2,4,56,7))