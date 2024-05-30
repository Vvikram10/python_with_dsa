n = int(input("Enter the size of array "))
array = []
for i in range(n):
    ele = int(input("Enter element "))
    array.append(ele)

print(array)

def sort_color(array):
    low = 0
    mid = 0
    high = len(array)-1

    while mid <= high:
        if array[mid] == 0:
            array[low],array[mid] = array[mid],array[low]
            low += 1
            mid += 1

        elif array[mid] == 1:
            mid += 1
        
        else:
            array[high],array[mid] = array[mid],array[high]
            high -= 1
    return array

print(sort_color(array))       