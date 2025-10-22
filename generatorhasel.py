import random
import string

signs = '!@#%^&*()-_=+~`<>?/\\|{}[];:"'

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    all_characters = string.ascii_letters + string.digits + signs
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(signs)
    ]
    if length > 4:
        password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

# Example usage:
print(generate_password(12))