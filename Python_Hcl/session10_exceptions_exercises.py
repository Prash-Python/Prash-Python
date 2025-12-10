# Exercise 1: Define an exception if the input age is less than the voting age.
# Method 1.
def defineException(age):
    if age < 18:
        raise ValueError(f"Entered Age {age} cannot be less than voting age")
    else:
        print(f"Eligible to vote for provided age: {age}")
defineException(int(input("Enter the age: ")))
