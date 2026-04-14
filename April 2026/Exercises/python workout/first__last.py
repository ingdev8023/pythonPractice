def first_last(sequence):
    return sequence[:1] + sequence[-1:]

print(first_last([1,2,3,4]))
print(first_last((1,2,3,6)))
print(first_last('abc'))


#testing size of a List
import sys
mylist = []
for i in range(25):
  l = len(mylist)
  s = sys.getsizeof(mylist)
  print(f'len = {l}, size = {s}')
  mylist.append(i)