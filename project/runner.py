# Import Components from Application
from project.app import *

def run():
    x = 3
    y = 5
    MATH = SimpleMath(x, y)
    print("Application Running")
    print(MATH.add())
    print(MATH.subtract())
    print(MATH.multiply())
    print(MATH.divide())
    print("Application Done Running")