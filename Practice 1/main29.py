# print even numbers from 1 to 10 and show the count of even numbers
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        count += 1

print(f"We have {count} even numbers")