alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

char_set = alphabet + numbers + special_characters


def caesar(original_text, shift_amount, encode_or_decode):
    """Encrypts or decrypts the message."""
    text_output = ""
    shifted_position = ""

    for letter in original_text:
        if letter in char_set:
            if encode_or_decode == "encode":
                shifted_position = char_set.index(letter) + shift_amount
            elif encode_or_decode == "decode":
                shifted_position = char_set.index(letter) - shift_amount
            shifted_position %= len(char_set)
            text_output += char_set[shifted_position]
        else:
            text_output += letter

    print(f"Here is your {encode_or_decode}d result: {text_output}")


def get_input_direction():
    """Gets direction to encode or decode from user input and checks if input is valid."""
    input_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while input_direction not in ['encode', 'decode']:
        print("It seems like your input has a typo. Please try again.")
        input_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    return input_direction


def get_input_shift():
    """Gets shift number from user input and checks if input is a number."""
    input_shift = input("Type the shift number:\n")

    if not isinstance(int(input_shift), int):
        print("It seems like your input was not a number. Please try again.")
        input_shift = input("Type the shift number:\n")

    return int(input_shift)


def get_input_restart():
    """Gets info to restart or ending the program from user input and checks if input is valid."""
    input_restart = input("Do you want to restart the cipher program and continue encrypting/decrypting?\n"
                    "Type 'yes' to continue or 'no' to end.\n").lower()

    while input_restart not in ['yes', 'no']:
        input_restart = input("Type 'yes' to continue or 'no' to end.\n").lower()

    return input_restart

