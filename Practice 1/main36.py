# filter function 

products = [
    ("first_product", 200),
    ("second_product", 400),
    ("third_product", 500),
    ("fourth_product", 100),
    ("fifth_product", 300),
]

# lets say if we want to create a list of products of which just the prices of the products is greater than 200 from the list(i.e. products), means we want to filter the data of products right now

x = filter(lambda data: data[1] > 200, products)
print(x) # <filter object at 0x000002BF3D861FA0>

x = list(filter(lambda data: data[1] > 200, products))
print(x) # [('second_product', 400), ('third_product', 500), ('fifth_product', 300)]
