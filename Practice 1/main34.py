# Sorting list with complex objects using lambda functions

data = [
    ("first_product", 200),
    ("second_product", 400),
    ("third_product", 500),
    ("fourth_product", 100),
    ("fifth_product", 300),
]


data.sort(key=lambda data:data[1]) 

print(data) # [('fourth_product', 100), ('first_product', 200), ('fifth_product', 300), ('second_product', 400), ('third_product', 500)]