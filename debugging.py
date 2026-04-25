'''  Packages & Debugging
       (1) Python Packages & Core Packages
       (2) Package manager & External Package
       (3) Debugging
'''

import turtle
print("========= Python Packages & Core Packages =========")
''' Python Packages / Modules: Core, File and External '''
# Core Packagees > https://docs.python.org/3/library

# Core packages
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)

# turtle.done()

print("-------")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content: ", content)
finally:
    my_file.close()

# with - Context meneger
# tepadagi mantiqmi try: ni oson yoli
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content: ", your_content)

print("DONE")