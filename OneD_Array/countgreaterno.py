n = int(input("Enter size of array: "))
array = []

for i in range(n):
    ele = int(input("Enter element: "))
    array.append(ele)

key = int(input("Enter key: "))
count = 0

for i in range(len(array)):
    if array[i] > key:
        count += 1

print("Number of elements greater than", key, "is:", count)
