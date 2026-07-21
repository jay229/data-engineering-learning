"""
    1. The only allowed characters in Python are
         alphabet symbols(either lower case or upper case)
         digits(0 to 9)
         underscore symbol(_)
        By mistake if we are using any other symbol like $ then we will get syntax error.
"""
name="Mritunjay"
print(name) # correct

# name@="Mritunjay"
# print(name) # Incorrect, TypeError: unsupported operand type(s) for @=: 'str' and 'str'


# name$="Mritunjay"
# print(name) # SyntaxError: invalid syntax


# Identifier should not starts with digit
# 1name="Jay"
# print(1name)
# SyntaxError: invalid decimal literal


# Identifiers are case sensitive
# name="Mritunjay"
# Name="Jay"
# NAME='mritunjay'
# print(name)
# print(Name)
# print(NAME)


