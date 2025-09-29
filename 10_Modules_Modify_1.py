"""
Filename: 10_Modules_Modify_1.py

Instructions:
This script contains two related functions for formatting text. It's getting a
bit crowded, and we want to make these functions reusable in other projects.

Your task:
1.  Create a NEW file in the same directory named `text_utils.py`.
2.  Cut (don't copy) the two functions (`shout` and `whisper`) from this
    file and paste them into `text_utils.py`.
3.  In this file (`10_Modules_Modify_1.py`), add an `import` statement at the
    top to import your new `text_utils` module.
4.  Modify the function calls on lines 31 and 32 so that they correctly use
    the functions from the `text_utils` module. (Hint: you will need to add
    a prefix).
5.  Run this file. The output should be exactly the same as before.
"""

# STARTING CODE

# TODO: Add an import statement here to import the `text_utils.py` module.


# TODO: Move these two functions to a new file called text_utils.py
def shout(message):
    """Converts a message to uppercase and adds exclamation points."""
    return message.upper() + "!!!"

def whisper(message):
    """Converts a message to lowercase and adds 'shh...'."""
    return "shh... " + message.lower()


# --- Main program execution ---
# TODO: Modify these function calls to work after moving the functions.
angry_message = shout("I need coffee")
secret_message = whisper("The eagle flies at midnight")

print(angry_message)
print(secret_message)
