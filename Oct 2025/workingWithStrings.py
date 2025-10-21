#Consider the variable d use slicing to print out the first three elements:
# Write your code below and press Shift+Enter to execute

d = "ABCDEFG"
d[0:3]

#Use a stride value of 2 to print out every second character of the string e:
# Write your code below and press Shift+Enter to execute

e = 'clocrkr1e1c1t'
e[::2]

#Consider the variable g, and find the first index of the sub-string snow:
# Write your code below and press Shift+Enter to execute

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find('snow')

# In the variable g, replace the sub-string Mary with Bob:
# Write your code below and press Shift+Enter to execute
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.replace('Mary', 'Bob')


#In the variable g, replace the sub-string , with .:
# Write your code below and press Shift+Enter to execute
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.replace(',' ,'.')

#In the variable g, split the substring to list:
# Write your code below and press Shift+Enter to execute
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.split()

#In the string <code>s3</code>, find whether the digit is present or not using the <code>\d</code> and <code>search() </code>function:
s3 = "House number- 1105"
# Write your code below and press Shift+Enter to execute
import re
pattern = r"\d\d\d"
match= re.search(pattern,s3)
match

#In the string <code>str1</code>, replace the sub-string <code>fox</code> with <code>bear</code> using <code>sub() </code>function:
str1= "The quick brown fox jumps over the lazy dog."

# Write your code below and press Shift+Enter to execute
import re
replace = re.sub(r'fox','bear',str1)
replace

#In the string str2 find all the occurrences of woo using findall() function:
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

# Write your code below and press Shift+Enter to execute
import re

find = re.findall('woo',str2)
find


def sum(x, y):
        return(x+y)
print(sum(sum(1,2), sum(3,4)))


print((10 >= 5*2) and (10 <= 5*2))