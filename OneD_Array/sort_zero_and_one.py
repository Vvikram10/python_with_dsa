n = int(input("Enter the size of array "))
array = []
for i in range(n):
    ele = int(input("Enter element "))
    array.append(ele)

print(array)

def sort(array):
    left = 0
    right = len(array)-1

    while left < right:
        if array[left] == 1 and array[right] == 0:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

        if array[left] == 0:
            left += 1 
        if array[right] == 1:
            right -= 1
    return array

print(sort(array))       