def encode(password):
    encoded = "".join(str((int(digit) + 3) % 10) for digit in password)
    return encoded


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
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")

        elif option == "3":
            break

        else:
            print("Invalid option. Please try again.")
