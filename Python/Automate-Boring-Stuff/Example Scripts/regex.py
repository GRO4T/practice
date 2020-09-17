import re

"""
Basic pattern matching
"""

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

"""
Grouping
"""

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')


mo = phoneNumRegex.search('My number is 415-555-4242.')

print("Printing different groups")
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

print('Phone number found: ' + mo.group()) # alternatively we can write mo.group(0)


"""
Pipes
"""

print("\nPipes")

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())

"""
? - match preceding group zero or one times
* - match preceding group zero or more times
+ - match preceding group one or more times

(some_text){number} will match some_text number times
e.g. (Ha){3} will match HaHaHa but not HaHa
"""

questionMarkRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
starRegex = re.compile(r'Bat(wo)*man')
plusRegex = re.compile(r'Bat(wo)+man')

numberRegex = re.compile(r'(Ha){3}')
numberRegex2 = re.compile(r'(Ha){3,5}') # you can define a range from 3 to 5 times
numberRegex3 = re.compile(r'(Ha){3,}') # three or more
numberRegex4 = re.compile(r'(Ha){,5}') # up to 5 times




