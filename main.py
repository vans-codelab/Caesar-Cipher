import art
import caesar_functions as cf

print(art.logo)
print("Welcome to Caesar Cipher! \n"
      "This tool lets you encrypt or decrypt your message. Let's start!\n")

continue_program = True

while continue_program:
    # Get user input
    direction = cf.get_input_direction()
    text = input("Type your message:\n").lower()
    shift = cf.get_input_shift()

    # Encrypt or decrypt the message
    cf.caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if user wants to continue
    restart = cf.get_input_restart()
    if restart == "no":
        continue_program = False
        print("Goodbye.")
