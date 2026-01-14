import re
import csv

# print(re.search(r"\w","hello"))
# print(re.search(r"Py.*n", "Python Programming"))
# print(re.search(r"o+l+", "woolly"))
# print(re.search(r"p?each", "To each their own"))
# print(re.search(r"p?each", "I like peaches"))
# print(re.search(r"\.com", "welcome"))
# print(re.search(r"\.com", "mydomain.com"))
# print(re.search(r"\w*", "This is an example"))
# print(re.search(r"\w*", "And_this_is_another"))
# print(re.search(r"A.*a", "Azerbaijan"))
# print(re.search(r"^A.*a$", "Australia"))
# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern, "_this_is_a_valid_variable_name"))
# print(re.search(pattern, "this isn't a valid variable"))
# print(re.search(pattern, "my_variable1"))

# def check_sentence(text):
#   result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
#   return result != None

# print(check_sentence("Is this is a sentence?")) # True
# print(check_sentence("is this is a sentence?")) # False
# print(check_sentence("Hello")) # False
# print(check_sentence("1-2-3-GO!")) # False
# print(check_sentence("A star is born.")) # True
# print(re.fullmatch(r""))

""" r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.


r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.


r”^/(.+)/([^/]+)/$” This line of code is often used to extract specific parts of URLs or file paths, such as the directory names or filenames. """

#first question
""" def check_web_address(text):
  pattern = r"^[\w\.\-\+][\w\.\-\+]*[\.a-zA-z]$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#2nd question
def check_time(text):
  pattern = r"^[1-9][1-9]*[:][0-5]+[0-9 ]+[Aa]?[Pp]?[Mm]+$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

#3rd question
def contains_acronym(text):
  pattern = r"\([A-Z][A-Za-z0-9]{1,}\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True



#4th question
def correct_function(text):
  result = re.search(r"\s\d{5}(-\d{4})?", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
 """
# print(re.split(r"the|a", "One sentence. Another one? And the last one!"))
# re.split(r"([.?!])", "One sentence. Another one? And the last one!")
# re.split(r"[.?!]", "One sentence. Another one? And the last one!")
# re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
# re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
#r"location.*(London|Berlin|Madrid)

# import re
# def transform_record(record):
#   new_record = re.sub(r"^([A-Za-z]+),([0-9-]+),([A-Za-z]+)$",r"\2",record)
#   return new_record

# print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# # Sabrina Green,+1-802-867-5309,System Administrator

# #1st question
# import re
# def transform_record(record):
#   new_record = re.sub(r"([0-9-]+)",r"+1-\1",record)
#   return new_record

# print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# # Sabrina Green,+1-802-867-5309,System Administrator

# print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# # Eli Jones,+1-684-3481127,IT specialist

# print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# # Melody Daniels,+1-846-687-7436,Programmer

# print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# # Charlie Rivera,+1-698-746-3357,Web Developer

# #2nd question
# import re
# def multi_vowel_words(text):
#   pattern = r"\w+[aeiou]{3}\w*"
#   result = re.findall(pattern, text)
#   return result

# print(multi_vowel_words("Life is beautiful")) 
# # ['beautiful']

# print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# # ['Obviously', 'queen', 'courageous', 'gracious']

# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# # ['rambunctious', 'quietly', 'delicious']

# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# # ['queue']

# print(multi_vowel_words("Hello world!")) 
# # []

# #3rd question
# import re
# def transform_comments(line_of_code):
#   result = re.sub(r"[#]+","//",line_of_code)
#   return result

# print(transform_comments("### Start of program")) 
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable")) 
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable")) 
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)")) 
# # Should be "  return(number)"

# #4th question
# import re
# def convert_phone_number(phone):
#   result = re.sub(r"(\d{3})-(\d{3})-(\d{4})(?!\d)",r"(\1) \2-\3", phone)
#   return result

# print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
# print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
# print(convert_phone_number("123-123-12345")) # 123-123-12345
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300



def contains_domain(address, domain):
  #Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False
def replace_domain(address, old_domain, new_domain):
#Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
def main():
#"""Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '/home/[virtual_machine_username]/data/user_emails.csv'
  report_file = '/home/[virtual_machine_username]/data' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()


def find_gov_urls(website):
 pattern = r"https?://[A-Za-z0-9.-]+\.gov" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []

def find_productID(report):
  pattern =r"\b1\d{3}-[A-Z]{2}-\d{2}\b"#enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result
  
print(find_productID("Products 1234-AB-30 and 2234-AB-30, not items 12-AB-30 or 12345-AB-30")) # Should return ['1234-AB-30']
print(find_productID("Products of interest are 1234-AB-30, 1678-XZ-11, and 1561-CD-57. We're not interested in other products like 2345-AB-29.")) # Should return ['1234-AB-30', '1678-XZ-11', '1561-CD-57']