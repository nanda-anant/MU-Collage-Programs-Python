
# Program to retrieve database records using
# fetchone(), fetchmany() and fetchall()

import mysql.connector

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

# Create cursor
cur = con.cursor()

print("Database connected successfully!")

# Execute SELECT query
cur.execute("SELECT * FROM student")

# 1. Fetch one record
print("\nUsing fetchone():")
record = cur.fetchone()
print(record)

# Execute query again
cur.execute("SELECT * FROM student")

# 2. Fetch multiple records
print("\nUsing fetchmany():")
records = cur.fetchmany(2)

for row in records:
    print(row)

# Execute query again
cur.execute("SELECT * FROM student")

# 3. Fetch all records
print("\nUsing fetchall():")
records = cur.fetchall()

for row in records:
    print(row)

# Close cursor and connection
cur.close()
con.close()

print("\nDatabase connection closed.")
