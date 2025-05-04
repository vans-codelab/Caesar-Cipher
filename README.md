# Caesar Cipher - Encrypting Messages
The Caesar Cipher is one of the oldest and most well-known encryption methods, named after Julius Caesar, who used it himself to send secret messages.

### How it Works
In the Caesar Cipher, the characters in the text are shifted by a desired number. This shift generates a new, encrypted text. The method is based on a simple but effective technique, where each character in the original text is replaced by a character that is a certain number of positions forward or backward in the alphabet.

**Example:** The text 'abc' becomes 'def' when shifted by 3 positions.

### Extended Character Set
To make the encryption more complex, the character set in this project has been extended. In addition to the classical letters of the Latin alphabet, numbers and special characters are also included, allowing a greater variety of characters to be encrypted. This extension increases the security and scope of the encryption, allowing for a broader range of characters to be encrypted.

### Benefits of the Caesar Cipher
- **Simplicity:** The Caesar Cipher is easy to understand and implement.
- **Extended Character Set:** The extended character set makes the encrypted text more difficult to crack.
- **Beginner Level:** Ideal for beginners and anyone wanting to get started with cryptography.

### Requirements
- **Programming Language:**
  The project was developed and tested with Python 3.11.  
  Python can be downloaded and installed from the official website: https://www.python.org/downloads/

- **Python Packages:**
  The project uses only Python's standard library, so no external libraries are required.

### Usage
1. **Download Files:**
   
   Click the green "Code" button on GitHub and download the repository as a ZIP file.  
   Extract the folder and ensure that all Python files are in the same directory.
   
2. **Run the Program:**
   
   Open the command prompt and navigate to the directory where the files are located.  
   Example:

       cd "C:\Caesar-Cipher\"

   Run **main.py** to start the program:
  
       python main.py

3. **Encrypt or Decrypt Text:**

    Choose whether to encrypt ("encode") or decrypt ("decode") the text. Then, enter the text and the desired shift to encrypt or decrypt it.

### Context
This project was developed as part of the "100 Days of Code - The Complete Python Pro Bootcamp" course by Angela Yu on Udemy, where I learned the basic concepts of Python programming. After completing the basic Caesar Cipher from the course, I decided to expand the project by adding additional features, such as supporting numbers and special characters in the encrypted text. To improve readability and structure, selected code blocks were refactored into functions and moved to a separate module. Furthermore, I considered the possibility of incorrect user inputs and adapted the code to handle these errors.

### German Version
For the German version of this README, please refer to [README_DE.md](https://github.com/vans-codelab/Caesar-Cipher/blob/side-branch/README_DE.md).
