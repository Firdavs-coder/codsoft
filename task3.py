import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lower + upper + digits + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    generated_password = ''.join(password)

    print(f"\nYour generated password is: {generated_password}")

generate_password()
