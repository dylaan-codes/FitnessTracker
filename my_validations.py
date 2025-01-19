# vcmd_validation.py

"""
Integer Validation: Allows empty input or only digits
"""
def validate_int(new_value):
    """Allow empty input (deletion) or only digits (integer input)."""
    if new_value == "" or new_value.isdigit():  # Allow empty or digits only
        return True
    return False


""" 
Float Validation: Allows empty input or a valid float (with one decimal point)
"""
def validate_float(new_value):
    """Allow empty input (deletion) or a valid float (one decimal point)."""
    if new_value == "" or new_value.count(".") <= 1:  # Allow empty or one dot
        try:
            if new_value == "":  # Handle empty case explicitly
                return True
            float(new_value)  # Check if it can be converted to a float
            return True
        except ValueError:
            return False
    return False



""" 
String Validation: Allows empty input or only alphabetic characters
"""
def validate_string(new_value):
    """Allow empty input (deletion) or only alphabetic characters (string input)."""
    if new_value == "" or new_value.isalpha():  # Allow empty or alphabetic only
        return True
    return False


"""
Function to strip leading and trailing spaces
"""
def validate_empty(*args):
    for value in args:
        if value.strip() == "":
            print("There are empty values (or contains only spaces).")
            return 1
    return 0


""" 
Function to register the validation commands for Tkinter
"""
def get_vcmd(root):
    """Return a dictionary with validation commands for integer, float, and string."""
    return {
        "int": (root.register(validate_int), "%P"),  # Register integer validation
        "float": (root.register(validate_float), "%P"),  # Register float validation
        "string": (root.register(validate_string), "%P")  # Register string validation
    }


