n = int(input("Size of array "))
array = []
for i in range(n):
    ele = int(input(f"enetr {i} element "))
    array.append(ele)
print("array ",array)    

i = 0
j = len(array)-1

while(i<=j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp 
    i += 1
    j -= 1

print("array ",array)       