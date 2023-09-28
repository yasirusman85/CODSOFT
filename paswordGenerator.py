import random
import string


def generate_password(length):
    # Define character sets for different complexities
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lower_case + upper_case + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        print("Password length must be at least 8 characters.")
        return

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


# Prompt the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid password length as an integer.")
