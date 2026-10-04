# Program to demonstrate basic regular expression pattern matching

import re

text = input("Enter a string: ")
pattern = input("Enter a pattern to search: ")

match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
    print("Starting position:", match.start())
else:
    print("Pattern not found")

print("Regular Expression Pattern Matching Completed...")