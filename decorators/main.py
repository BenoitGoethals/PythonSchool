from datetime import time



def calcutate(func):
    def wrapper(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        res=func(*args, **kwargs)
        # Log the return value
        print(f"{func.__name__} returned: {res}")

        return str(res) +" result"
    return wrapper

@calcutate
def add(a, b):
    return a + b


def start():
    print(add(5,4))



if __name__ == '__main__':
    start()


