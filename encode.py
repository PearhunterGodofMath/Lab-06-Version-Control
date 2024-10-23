# Team Member: David Campbell

def encode(password):
    encoded_password = ""
    for char in password:
        encoded_digit = (int(char) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid password. Please enter an 8-digit number.")

        elif option == "2":
            # original_password = decode(encoded_password)
            # print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")

        elif option == "3":
            break