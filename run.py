# Primitive variables

# print("PYTHON: Everything is Object")

# DUNDERS(Double Underscore)   &   __BUILTINS__ ,  &  __init__

# Dunder -> Pythonni ichki  quriliah mexanizmi

# __BUILTINS__ -> print(), type() lar kiradi

message = "PYTHON: Everything is Object"
print(message)

result = type(message)
print("result: ", result)

'''
In Python, there are builtin tools:

(1) TYPES => int float str list dict
(2) FUNCTIONS => print() type() len() range() input() etc.  
(3) CONATANTS => None True False   
'''

print(dir(__builtins__))
