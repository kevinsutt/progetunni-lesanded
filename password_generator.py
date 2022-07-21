# keyboard letters, numbers, special characters
# rules? length? special minimum characters? no words?
import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!@#$%^&*()")
characters_total = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    length = int(input("Password length: "))
    letter_count = int(input("Amount of letters in the password: "))
    special_characters_count = int(input("Amount of special characters in the password: "))
    number_count = int(input("Amount of numbers in the password: "))
    total_count = (letter_count + special_characters_count + number_count)
    # return goes back to start if needed
    if total_count > length:
        print("Total characters are greater than the length. Please set new numbers.")
        return
    
    password = []
    for i in range(letter_count):
        password.append(random.choice(letters))
        
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))
        
    for i in range(number_count):
        password.append(random.choice(numbers))
    # not enough  
    if total_count < length:
        print("You did not add enough characters to make the password long enough for the length. Please set new numbers.")
        return
    random.shuffle(password)
    print("".join(password))
    
    
    
# start the function
generate_password()
        
