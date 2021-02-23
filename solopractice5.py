## Regular Expressions
# Regular expressions are tools used for string manipulation.
# They are a domain specific language (DSL) that is present as a library in most programming languages
# They are used for two tasks:
# 1. Verifying that strings match a pattern (for instance, that a string has the format of an email address)
# 2. Performing substitutions in a string (such as changing all American spellings to British ones)
# DSL languages are highly specialized mini programming languages. Regular expressions are an example of them, and SQL (for database manipulation) is another
# Private domain-specific languages are often used for specific industrial purposes.

# Regular expressons in Python can be accessed using the re module, which is part of the standard library.
# After a regular expression is defined, the re.match function can be used to determine whether it matches at the beginning of a string. If it does, match return an object representing the match, if not, it returns None
#To avoid any confusion while working with regular expressions, we would use raw strings as r"expression". Raw strings don't escape anything, which makes use of regular expressions easier

#Example where it checks whether the pattern "spam" matches the string:

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")

# Other functions to match patterns are re.search and re.findall
# re.search finds a match of a pattern anywhere in the string.
# re.findall returns return a list of all substrings that match a patterns.
# Example

import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("matchpattern Match")
else:
    print("matchpattern No Match!")

if re.search(pattern, "eggspamsausagespam"):
    print("searchpattern Match")
else:
    print("searchpattern No match")

if re.findall(pattern, "eggspamsausagespam"):
    print("findallpattern Match")
else:
    print("findallpattern No match")

#in the above code, matchpattern did not find a match because it looks at the beginning of a string

# regular expressions (regex) search returns an object with several methods that give details about it. 
# These methods include "group" which returns the string matched, "start" and "end" which return the start and ending positions of the first match, and 'span' which returns the start and end positions of the first match as a tuple.
# Example:

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

# most important 're' method that uses regular expressions is called 'sub' (substitute)
# sub syntax: re.sub(pattern, repl, string, count=0)
# this 'sub' method replaces all occurences of the 'pattern' in string with 'repl', substituting all occurences, unless 'count' provided. This method returns the modified string:

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

## Simple metacharacters
# Metacharacters are what make regular expressons more powerful than normal string methods. They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel."
# Existence of metacharacters poses a problem if you want to create a regular expression (regex) that matches a literal metacharacter, such as "$". This can be done by escaping the metacharacters by putting a backslash in front of them.
# This can also create a problem because backslashes also have an escaping function in normal Python strings. This can mean putting three or four backslashes in a row to do all the escaping.
# To avoid this problem, one can use a 'raw' string, which is a normal string with an "r" in front of it, just like the once used in the "re" method.

# For example, the "." metachacter matches any character, other than a new line:

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1 aa")
if re.match(pattern, "gray"):
    print("Match 2 aa")
if re.match(pattern, "blue"):
    print("Match 3 aa")

# next metacharacters are '^' and '$'  => these match the start and end of a string, respectively.

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1 bb")
if re.match(pattern, "gray"):
    print("Match 2 bb")
if re.match(pattern, "stingray"):
    print("Match 3 bb")

## Character classes
# character classes provide a way to match only one of a specific set of characters
# a character class is created by putting the characters it matches inside square brackets.

import re

pattern  = r"[aeiou][y]"

if re.search(pattern, "grey"):
    print("Match 1 cc")

if re.search(pattern, "qwertyuiop"):
    print("Match 2 cc")

if re.search(pattern, "rhytm myths"):
    print("Match 3 cc")

# Quiz: What would [abc][def] match? => Any letter out of "abc", then any out of "def"

# Character classes can also match ranges of characters. Some examples:
# Class [a-z] matches any lowercase alphabetic character
# Class [G-P] matches any uppercase character from G to P
# Class [0-9] matches any digit
# Multiple ranges can be included in once class, e.g. [A-Za-z] matches a letter of any case.

import re

pattern  = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1 dd")

if re.search(pattern, "E3"):
    print("Match 2 dd")

if re.search(pattern, "1ab"):
    print("Match 3 dd")

# Place a "^" at the start of a character to invert it. This causes it to match any character other than the ones included. 
# Other metacharacters suc as "$" and "." have no meaning iwthin character classes. The "^" metacharacter has no meaning unless it is the first character in a class.

import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1 ee")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2 ee")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3 ee")

# more  metacharacters are: * + ? { }
# these specify the number of repetitions. 
# * metacharacter means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses.
# Example:

import re

pattern  = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1 ff")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2 ff")

if re.match(pattern, "spam"):
    print("Match 3 ff")

# the example above matches the strings that start with "egg" and follow with zero or more "spam"s.

# the metacharacter '+' is very similar to '*', except it means "one or more repetition", as opposed to zero or more repetitions.

import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1 gg")

if re.match(pattern, "ggggggggggggg"):
    print("Match 2 gg")

if re.match(pattern, "abc"):
    print("Match 3 gg")

# To summarize:
# * matches 0 or more occurrences of the preceding expression.
# + matches 1 or more occurrence of the preceding expression.

# ? matches 0 or more repetitions

import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1 hh")

if re.match(pattern, "icecream"):
    print("Match 2 hh")

if re.match(pattern, "sausages"):
    print("Match 3 hh")

if re.match(pattern, "ice--ice"):
    print("Match 4 hh")

# curly braces can be used to represent the number of repetitions between two numbers.
# regex {x,y} means "between x and y repetitions of something"
# Hence {0,1} is the same things as ?.
# If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.

import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1 ii")

if re.match(pattern, "999"):
    print("Match 2 ii")

if re.match(pattern, "9999"):
    print("Match 3 ii")

## Groups
# Groups can be created by surrounding part of a regular expression with parentheses. This means that a group can be given as an argument to metacharacters such as '*' and ?.

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1 jj")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2 jj")

if re.match(pattern, "spam"):
    print("Match 3 jj")

# above, (spam) represents a group

# The content of groups in a match can be accessed using the group function. 
# A call of group(0) or group() returns the whole match. A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups() returns all groups up from 1.

import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

# Special groups => two useful ones are 'named groups' and 'non-capturing groups'.
# Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. The behave the same way as normal groups, except they can be accessed by group(name) in addition to its number.
# Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

# Another important metacharacter is '|'
# '|' means "or", so red|blue matches either "red" or "blue"

import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match 1 kk")

match = re.match(pattern, "grey")
if match:
    print("Match 2 kk")

match = re.match(pattern, "griy")
if match:
    print("Match 3 kk")

## Special sequences
# Special sequences are written as a backslash followed by another character.
# For example, a useful special sequence is a backslash and a number between 1 and 99, e.g. \1 or \17. This matches the expression of the group of that number.

import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")

if match:
    print("Match 1 ll")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2 ll")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3 ll")

# more useful special sequences are \d, \s, \w (digits, whitespace, word characters)
# \w matches letters with accents as well.
# with uppercase letters, such as \D, \S, \W mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.

import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1 mm")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2 mm")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3 mm")

# the code above matches one or more non-digits, followed by a digit.

# Additional special sequences are \A, \Z, and \b
# The sequences \A and \Z match the beginning and end of a string, respectively. 
# Sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
# Sequence \B matches the empty string anywhere else.

import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1 nn")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2 nn")

match = re.search(pattern, "We scattered.")
if match:
    print("Match 3 nn")

# basically, \b(cat)\b matches the word "cat" surrounded by word boundaries

import re

pattern = r"\AS...\b.\Z"

match = re.search(pattern, "SPAM!")
if match:
    print("YESS")

## Email extraction
# pattern for extracting email from string:
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

str = "Please contact info@medappl.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())

# a basic email address consists of a word and may include dots or dashes. This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix). 
# [\w\.-]+ matches one or more word character, dot or dash. 
# regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign, then another similar word, then a dot and another word. 
# In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses. 


# Question: What would be matched by "(4{5,6}\1" => 10 or 12 fours

## Phone number validator => You are given a number input, and need to check if it is a valid phone number.
# A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
# Output "Valid" if the number is valid and "Invalid", if it is not.

# Sample Input
# 81239870

# Sample Output
# Valid

# import re

# int = input()

# pattern = "(1|8|9)(\d{7})$"

# match = re.match(pattern, int)
# if match:
#     print("Valid")
# else:
#     print("Invalid")

