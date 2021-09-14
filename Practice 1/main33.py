# Sorting list with complex objects using simple functions

data = [
    ("first_product", 200),
    ("second_product", 400),
    ("third_product", 500),
    ("fourth_product", 100),
    ("fifth_product", 300),
]

def sort_data(data):
    return data[1]


data.sort(key=sort_data)

print(data) # [('fourth_product', 100), ('first_product', 200), ('fifth_product', 300), ('second_product', 400), ('third_product', 500)]