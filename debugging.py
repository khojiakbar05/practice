'''  Packages & Debugging
       (1) Python Packages & Core Packages
       (2) Package manager & External Package
       (3) Debugging
'''

from PIL import Image
import turtle

print("========= Python Packages & Core Packages =========")
''' Python Packages / Modules: Core, File and External '''
# Core Packagees > https://docs.python.org/3/library
# Core packageslar PYTHONNI ozi bilan birga keladi

# Core packages
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.circle(100)

turtle.done()

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


print("========= Package manager & External Package =========")
# External packages > https://pypi.org/
''' Package manager 
     Python => pip pipenv
     NodeJs => npm yarn
     PHP    => composer
     MacOS  => brew
'''
# pillow -> package rasmlar bilan birga ishlash uchun ishlatiladi


with Image.open("material/logo.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")


print("========= Debugging =========")


def get_summary(*args): # define
    total_amount = 0
    for a in args:
        total_amount +=a
        return total_amount  # Find the bug via debugging

test = 100
result = get_summary(1, 2, 3, 4, 5) # call
print("result: ", result)