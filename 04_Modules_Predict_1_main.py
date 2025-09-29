"""
Filename: 04_Modules_Predict_1_main.py

Instructions:
This is the main script. It imports the module from the file
`03_Modules_Predict_1_greetings.py`.

Read the code below. Without running it, predict what the final output will be
in the terminal. Write down your prediction and your reasoning.
"""

# We are importing the code from the other file.
# Make sure both files are in the same directory.
import greetings

print("The main program is starting...")

# We are calling a function that is defined in the other file.
greetings.say_hello()

print("The main program is ending.")
