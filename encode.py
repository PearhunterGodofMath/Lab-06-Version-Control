# Encode by David Campbell
# Decode by Megha Ramprasad

def encode(password):
    encoded_password = ""
    for char in password:
        encoded_digit = (int(char) + 3) % 10 # Shifts each digit up by 3.
        encoded_password += str(encoded_digit) # Puts all the encoded digits in order.
    return encoded_password

def decode(password):
    string = ''
    for item in password[0:9]: # limit to 8
        string += str((int(item[0] - 3) % 10)) # accepts number, subtracts 3, mod 10, returns the number - 3
    return str(string)

def main():
    while True: # Prints Menu Options.
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = input("Please enter an option: ") # User chooses an option.

        if option == "1": # Encodes user inputted password.
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit(): # Needs to be an 8-digit password.
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else: # Not 8-digits.
                print("Invalid password. Enter an 8-digit number.")

        elif option == "2": # Uses the encoded password and decodes it.
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")

        elif option == "3": # Ends the program.
            break
