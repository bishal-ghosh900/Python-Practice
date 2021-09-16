# decorators in depth
from functools import wraps

# decorators are the function which takes function as an argument and returns function also

def decoratingWithIteration(times): # Its the custom decorator factory which return a decorator and its mainly used to take the input number to know how many times the code under wrapper function should run
    def decorator(fn): # => creating the decorator 
        @wraps(fn) # => its to maintain the definition remain same for the run method, not to change to as the wrapper function is.
        def wrapper(*args):
            for i in range(times):
                legs = fn(*args)
                print(f"I am running with {legs} legs")
        return wrapper
    return decorator

@decoratingWithIteration(int(input("How many numbers you want to see: "))) # => usage of the decorator . Its the same as (after defining run() method) -> run = decorator(run) 
# -> means we are decorating run method and after the decorations we will return it
def run(legs = 2):
    return legs 

run(int(input("Give the number of legs: ")))

from functools import wraps

