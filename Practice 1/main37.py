# list comprehension 

# previously in main35.py and main36.py we learned how to use map and filter function using functional programming( lambda functions )
# 
# Now We are going to use list comprehension to implement the feature of map() and filter() function but in a more neat and flexible way  

products = [
    ("first_product", 200),
    ("second_product", 400),
    ("third_product", 500),
    ("fourth_product", 100),
    ("fifth_product", 300),
]

# x = [ expression for i in range()]

# map implementation using list comprehension
x1 = [i[1] for i in products]
print(x1) # [200, 400, 500, 100, 300]

# filter implementation using list comprehension
x2 = [i for i in products if (i[1] > 200)]
print(x2) # [('second_product', 400), ('third_product', 500), ('fifth_product', 300)]
