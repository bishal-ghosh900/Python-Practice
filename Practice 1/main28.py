# for-else

for i in range(1, 5):
    print(i)
    if i == 4:
        break
    else:
        continue
else:
    print("Nothing exactly happened")

#if there is not any break inside the for loop, then the else condition will definitely run