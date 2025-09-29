"""
Filename: 06_Modules_Predict_2_main.py

Instructions:
This exercise demonstrates a "name collision". This script imports a function
named `do_calculation` from the `05_Modules_Predict_2_calculator.py` file.
However, it then defines its OWN function with the exact same name.

When `main.py` is run, which `do_calculation` function will be used on the
last line? Predict the final output of the script.
"""

# This imports the specific function from the other file.
from calculator import do_calculation

# Uh oh, we are defining another function with the EXACT same name.
# Python uses the most recent definition it has seen.
def do_calculation():
    """The main script's version of the function."""
    return "This is the result from the 'main' script."


# Which function gets called here? The imported one or the one we just defined?
result = do_calculation()
print(result)
