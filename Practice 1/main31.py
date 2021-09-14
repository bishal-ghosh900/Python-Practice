# Non-keyworded variable-length arguments and keyworded variable-length arguments

def show( *n1, **n2 ):
    print(f"{n1} {n2}")

show(1, 2, 3, 4, 5, a = 6, b = 7, c = 8) # (1, 2, 3, 4, 5) {'a': 6, 'b': 7, 'c': 8}

# here 1, 2, 3, 4, 5 are the elements of the tupple( n1 ) which is being created by using * before n1;
# here a = 6, b = 7, c = 8 are the elements of the dictionary which is being created by using ** before n2;