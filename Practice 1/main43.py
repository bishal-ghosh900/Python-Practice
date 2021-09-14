# dictionary comprehension

prods = dict(
    first_product=200,
    second_product=300,
    third_product=100,
    fourth_product=400,
)

vals2 = { k : v for k, v in prods.items() if v > 200}
print(vals2) # {'second_product': 300, 'fourth_product': 400}