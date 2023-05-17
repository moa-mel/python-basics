letter = 'p'
print(letter)
print(len(letter))

greeting = 'Hello, world!'
print(greeting)
print(len(greeting))

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
#mutltilineString
multiline_string = '''I am a teacher and enjoy teaching.I didn't find anything as rewarding as empowering people.That is why I created 30 days of python.'''
print(multiline_string)
#string concatenation
first_name = 'Asabeneh'
last_name = "Yetayeh"
full_name = first_name + ' ' + last_name 
print(full_name)
print(letter+ ' ' + greeting)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))

# \n: new line
# \t: Tab mean(8 spaces)
# \\\\: Back slash
# \\': Single quote (')
# \\": Double quote (")
print('I hope everyone is enjoying the Python Challenge. \nAre you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
# To write a backslash
print('This is a backslash symbol (\\)')
# to write a double quote inside a single quote
print('In every programming language it starts with \"Hello, World!\"')
print('I am a creative genius \"Software Engineer\"')

# capitalize(): Converts the first character the string to Capital Letter
# capitalize(): Converts the first character the string to Capital Letter
challenge = 'thirty days of python'
print(challenge.capitalize())

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Returns the index of first occurrence of substring
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * (radius ** 2)
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)
#isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'thirty days of python'
print(challenge.isalnum())
challenge = 'thirty days of python 2019'
print(challenge.isalnum())
#isalpha(): Checks if all characters are alphabets
challenge = 'thirty days of python'
print(challenge.isalpha())
num = '123'
print(num.isalpha())
#isdecimal(): Checks Decimal Characters
num = '10'
print(num.isdecimal())
num = '10.5'
print(num.isdecimal())
#isdigit(): Checks Digit Characters
challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
# isidentifier(): Checks for valid identifier mean it check if a string is a valid variable name
challenge = "30DaysOfPython"
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
#islower(): Checks if all alphabets in a string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'thirty days of python'
print(challenge.islower())
#isupper(): return if all character are uppercase characters
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())
# isnumeric(): checks numeric character
num = '10'
print(num.isnumeric())
print('ten'.isnumeric())
# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)
#strip(): removes both leading and trailing characters
challenge = 'thirty days of python'
print(challenge.strip('y'))
#replace(): replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))
# split(): Splits Strings from left
challenge = 'thirty days of python'
print(challenge.split())
# title(): Return a Title Cased String
challenge = 'thirty days of python'
print(challenge.title())
# swapcase(): Checks if String Starts with Specified String
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())
# startswith(): Checks if String Starts with Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))

