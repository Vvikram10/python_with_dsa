print("Enter the size of array")
n = int(input("size of array "))
array = []

for i in range(n):
    ele = int(input("element is "))
    array.append(ele)  # Append the actual input element

max_value = array[0]  # Initialize max_value with the first element of the array

for i in range(1, len(array)):  # Start loop from the second element
    if array[i] > max_value:
        max_value = array[i]

print("max is ", max_value)
