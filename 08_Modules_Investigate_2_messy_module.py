"""
Filename: 08_Modules_Investigate_2_messy_module.py

This file demonstrates a module with a "side effect". It not only defines a
function, but it also contains a `print()` statement at the "top level" of
the file (meaning, not inside any function). This file is intended to be
imported by `09_Modules_Investigate_2_main.py`.
"""

def useful_function():
    print("This is a useful function.")

# This is "top-level" code.
# It runs the moment the file is imported by another script.
print("This message runs on import!")
