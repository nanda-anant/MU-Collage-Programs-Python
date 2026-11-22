
# Program to define and raise user-defined exceptions

# Define a user-defined exception
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    # Raise exception if age is less than 18
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    else:
        print("You are eligible to vote.")

except InvalidAgeError as e:
    print("User Defined Exception:", e)

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("Program execution completed.")
