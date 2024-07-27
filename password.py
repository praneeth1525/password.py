import random
import string

# Prompt the user to specify the desired length of the password
length = int(input("Please enter the desired length of the password: "))

# Generate Password
def generate_password(length):
    # Define the possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate and display the password
password = generate_password(length)
print(f"Generated password: {password}")
