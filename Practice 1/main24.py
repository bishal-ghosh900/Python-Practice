# Dictionary 

emp = {
    "id": 101,
    "first_name": "Bishal",
    "last_name": "Ghosh",
}


# key should be unique

print(emp) # {'id': 101, 'first_name': 'Bishal', 'last_name': 'Ghosh'}

print(emp["id"]) # 101
emp["id"] = 102
print(emp["id"]) # 102

print(emp.get("id"))  # 102

print(emp.get("address")) # None --> None is an object which represent abscence of value, as we don't have key like "address" in emp dictionary , thats why we are getting this None object. If we would have used emp["address"] to get the value of the key "address" which is not present in emp dictionary then we would have get an error, so to avoid error we supposed to use get() method.

# And if we provide any value as a second argument to get() method, then that value will be a default value for that particular key in that instant of time (immutable chnage) only , Ex -->


print(emp.get("address", "Kolkata")) # Kolkata
print(emp) # {'id': 102, 'first_name': 'Bishal', 'last_name': 'Ghosh'} --> there is not any "address key"


Points = dict(x = 1, y = 2, z = 3 )
print(Points) # {'x': 1, 'y': 2, 'z': 3}

# looping through dictionary 
for i in Points:
    print(i,Points[i])
# output ->
# x 1
# y 2
# z 3

for key , value in Points.items():
    print(key, value)
#output ->
# x 1
# y 2
# z 3