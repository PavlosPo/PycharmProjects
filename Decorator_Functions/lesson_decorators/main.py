# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args})")
        result = function(*args)
        print(f"It returned: {result}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def calculate(*args):
    current_number = 1
    for arg in args:
        current_number = current_number *  arg
    return current_number


calculate(2,3,4,5,7)