# Tavienne Millner (encode function)
# Partner (decode function)


def main():
    # Lists to help the encode/decode process.
    password_chars_original = []
    password_chars_encoded = []

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
            password_to_encode = input("Please enter your password to encode: ")

            for char in password_to_encode:
                password_chars_original.append(int(char))
                password_chars_encoded.append(int(char)+3)
            print("Your password has been encoded and stored!")

            for i in range(len(password_chars_encoded)):
                password_chars_encoded[i] = str(password_chars_encoded[i])

        elif user_input == "2":
            # decode to be done by partner, if it's a two digit number, take the last digit.
            pass

        # Exits program
        elif user_input == "3":
            exit()


# Calls the main function.
if __name__ == "__main__":
    main()
