
# Program to plot Line, Bar, Histogram and Pie charts

import matplotlib.pyplot as plt

# Data
students = ['Anant', 'Jeet', 'Rahul', 'Amit', 'Jay']
marks = [85, 90, 75, 80, 95]

# 1. Line Chart
plt.figure(figsize=(6, 4))
plt.plot(students, marks, marker='o')
plt.title("Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Histogram
plt.figure(figsize=(6, 4))
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Pie Chart
plt.figure(figsize=(6, 4))
plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
