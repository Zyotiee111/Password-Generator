import string
import random

chars = string.ascii_letters
numbers = string.digits
specials = string.punctuation


length = int(input("Enter length of a password:"))

password = []
password.extend(list(chars))
password.extend(list(numbers))
password.extend(list(specials))

print("Your password is:","".join(random.sample(password,length)))
