n = int(input("Enter the size of array 1: "))
arr1 = []
for i in range(n):
    ele = int(input("Enter element: "))
    arr1.append(ele)

print("Array 1:", arr1)

m = int(input("Enter the size of array 2: "))
arr2 = []
for i in range(m):
    ele = int(input("Enter element: "))
    arr2.append(ele)

print("Array 2:", arr2)

def merge_arr(arr1, arr2):
    i, j = 0, 0
    merged_array = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append remaining elements of arr1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append remaining elements of arr2
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

result = merge_arr(arr1, arr2)
print("Merged array:", result)
