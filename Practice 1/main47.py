# one array is given , if in this array any 0 is present then push all those zero to the right of the array

# Input : [1, 4, 6, 3, 0, 3, 9, 0, 2, 7, 9]
# Output : [1, 4, 6, 3, 3, 9, 2, 7, 9, 0, 0]

n = int(input("Enter how many elements you want in the list: "))

arr = [int(input()) for i in range(0,n)]

st1 = ""
st2 = ""

for i in arr:
    if i != 0:
        st1 += str(i)
    else:
        st2 += str(i)

res = [int(i) for i in (st1 + st2)]

print(res)