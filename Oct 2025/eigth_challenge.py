# 1st question

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename[:filename.index("hpp") + 1])        
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#2nd question with comprehension

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [filename[:filename.index("hpp") + 1] if filename.endswith("hpp") else filename for filename in filenames]  # Start your code here


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# 3rd question
# Create a function that turns text into pig latin. Pig latin is a simple text transformation that modifies each word by:

# moving the first character to the end of each word;

# then appending the letters "ay" to the end of each word.

# For example, "python" ends up as "ythonpay".

# Make sure that there is no trailing whitespace at the end of the return output.

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  new = []
  for word in words:
    # Create the pig latin word and add it to the list
    new.append(word[1:] + word[0] + "ay")
    # Turn the list back into a phrase
  say = " ".join(new)
  return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("writing interesting functions")) # should be ritingway nterestingiay unctionsfay.