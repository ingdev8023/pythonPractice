def find_item(list, item):
 #Returns True if the item is in the list, False if not.
  if len(list) == 0:
   return False


 #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
   return True


 #Is the item in the first half of the list?
  if item < list[middle]:
   #Call the function with the first half of the list
   return find_item(list[:middle], item)
  else:
   #Call the function with the second half of the list
   return find_item(list[middle+1:], item)


  return False


#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]


print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False



#the fix was to sort the list

def find_item(list, item):
  list_sorted = sorted(list)
 #Returns True if the item is in the list, False if not.
  if len(list_sorted) == 0:
   return False


 #Is the item in the center of the list?
  middle = len(list_sorted)//2
  if list_sorted[middle] == item:
   return True

 #Is the item in the first half of the list?
  if item < list_sorted[middle]:
   #Call the function with the first half of the list
   return find_item(list_sorted[:middle], item)
  else:
   #Call the function with the second half of the list
   return find_item(list_sorted[middle+1:], item)


  return False


#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]


print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
