import re

text = "Python is easy. Python is powerful. I love Python."

pattern = "Python"

result1 = re.match(pattern, text)

if result1:
    print("match(): Pattern found at the beginning")
else:
    print("match(): Pattern not found at the beginning")

result2 = re.search(pattern, text)

if result2:
    print("search(): Pattern found:", result2.group())
else:
    print("search(): Pattern not found")

result3 = re.findall(pattern, text)

print("findall(): All occurrences:", result3)
print("Total occurrences:", len(result3))