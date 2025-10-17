def decorator_with_args(func):
    def wrapper(name):
        print("Function is about to run")
        func(name)
        print("Function has finished running")
    return wrapper
@decorator_with_args
def greet(name):
    print(f"Hello, {name}!")
greet("Mathesh")
