array = [1, 2, 3, 6, 4, 5]
print(array[1])
n = len(array)
print(n)

for i in range(n):
    print(array[i])

print(array[1:4])
array.sort(reverse=True)
print(array)