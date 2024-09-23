import numpy as np 
class Execute:
    def __init__(self):
        pass
    def say_hello(self, name, my_name):
        print(f"Heloo, {name}, I am {my_name}")
    def say_bye(self, name):
        print(f"Bye, {name}")
    def execute(self, func, *args):
        return func(*args)
executor = Execute()
executor.execute(executor.say_hello, "Peter", "George")
executor.execute(executor.say_bye, "Peter")

