"""
Filename: 09_Modules_Investigate_2_main.py

Instructions:
This script imports `08_Modules_Investigate_2_messy_module.py`.
Run this script and observe the output.

Answer the following questions:

1.  This file only has three lines of code. Why was "This message runs
    on import!" printed to the screen?

2.  When does the code inside `messy_module.py` get executed?

3.  Section 7.3 in the textbook discusses a special `if` statement that can
    prevent this side effect. What is that `if` statement, and how would you
    use it in `messy_module.py` to stop the message from printing on import?
"""

print("Main program is about to import...")

# The code in messy_module.py runs at this line!
import messy_module

print("Main program has finished importing.")

# We can still use the functions from the module
messy_module.useful_function()
