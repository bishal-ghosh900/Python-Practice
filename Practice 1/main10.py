# Weight converter

weight = int(input("Give me the weight value: "))

unit = input("Give me the unit(lbs(L) or kg(K)): ").lower()

if unit == "l" or unit == "lbs":
    print(f"Weight is {weight * 0.45} kg")
elif unit == "k" or unit == "kg":
    print(f"Weight is {weight / 0.45} pounds")
else:
    print("Not a valid unit")
