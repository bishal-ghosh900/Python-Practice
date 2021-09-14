# map function 

data = [
    ("first_product", 200),
    ("second_product", 400),
    ("third_product", 500),
    ("fourth_product", 100),
    ("fifth_product", 300),
]

# lets say if we want to create a list of just the prices of the products from the list(data)

x = map(lambda data:data[1], data) # It will just create the map object, if we print x now then we will get object related info and its address
print(x) # <map object at 0x000001E7A0C81FA0>

x = list(map(lambda data:data[1], data)) # If we use list() function then we will be able to create the list
print(x) # [200, 400, 500, 100, 300]
