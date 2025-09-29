"""
Filename: 11_Modules_Modify_2.py

Instructions:
This program uses the `math` module to perform a calculation. It currently
imports the entire module.

Your task is to modify the code to only import the specific tools we need.

1.  Change the `import math` statement to a `from...import...` statement that
    imports only the `pi` constant and the `pow` function.
2.  Remove the `math.` prefix from the line where `volume` is calculated,
    since we no longer need it.
3.  Run the code to ensure the output is the same.
"""

# STARTING CODE
# TODO: Modify this import statement.
import math

def sphere_volume(radius):
    """Calculates the volume of a sphere."""
    # The formula for the volume of a sphere is (4/3) * pi * r^3
    # TODO: Modify this line to remove the module prefix.
    volume = (4/3) * math.pi * math.pow(radius, 3)
    return volume

# --- Main program execution ---
r = 5
vol = sphere_volume(r)
print(f"The volume of a sphere with radius {r} is {vol:.2f}.")
