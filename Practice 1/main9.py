# Logical operator

true = True
false = False

if true and true:
    print("It is true") # and -> && 
else:
    print("It is false") # and -> && 

# Output --> It is true

if true or false:
    print("It is true") # and -> || 
else:
    print("It is false") # and -> || 

# Output --> It is true

if true and not true:
    print("It is true") 
    # and -> && 
    # not -> ! 
else:
    print("It is false") # and -> && 

# Output --> It is false

if true or not true:
    print("It is true") 
    # and -> &&
    # not -> !  
else:
    print("It is false") # and -> && 

# Output --> It is true