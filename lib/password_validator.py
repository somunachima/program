# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):
    exclamation = "!"
    at_sign = "@"
    dollar = "$"
    percent = "%"
    and_sign = "&"
    return (len(password) > 7) and (exclamation in password or at_sign in password or dollar in password or percent in password or and_sign in password)
    

