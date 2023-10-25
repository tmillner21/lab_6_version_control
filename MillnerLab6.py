# Tavienne Millner (encode function)
# Anya Whitman (decode function)


# Encode function.
def encode(password_to_encode):
    # List to help the encode process.
    password_chars_encoded = []

    for char in password_to_encode:
        password_chars_encoded.append(str(int(char) + 3))
    print("Your password has been encoded and stored!")

    return password_chars_encoded


# Decode function.
def decode(encoded_password):
    password_chars_decoded = []

    for char in encoded_password: #need to subract 3 from each encoded number
        if char == "0": #the encoded number resulted in 10
            password_chars_decoded.append("7")
        elif char == "1": #the encoded number resulted in 11
            password_chars_decoded.append("8")
        elif char == "2": #the encoded number resulted in 12
            password_chars_decoded.append("9")
        else: #the decoded number is the encoded number - 3
            password_chars_decoded.append(str(int(char)-3))

    return password_chars_decoded


# Main function.
def main():

    # A while loop so the program runs until the user chooses to stop.
    while True:

        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""""")
        user_input = input("Please enter an option: ")

        # If/else logic depending on the user's input.
        if user_input == "1":
            # Gets user's password to encode.
            password_to_encode = input("Please enter your password to encode: ")

            # List of encoded characters.
            password_chars_encoded = encode(password_to_encode)

            # Creating the encoded password string.
            encoded_password = ""
            for char in password_chars_encoded:
                encoded_password += char[-1]

        elif user_input == "2":
            # Gets user's password to decode.
            password_to_decode = input("please enter a password to decode: ")

            # List of decoded characters.
            password_chars_decoded = decode(password_to_decode)

            # creating the decoded password string.
            decoded_password = ""
            for char in password_chars_decoded:
                decoded_password += char

            # Displaying the decoded password.
            print(decoded_password)

        # Exits program
        elif user_input == "3":
            exit()


# Calls the main function.
if __name__ == "__main__":
    main()
