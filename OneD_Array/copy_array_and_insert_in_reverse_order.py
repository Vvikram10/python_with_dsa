n = int(input("Size of array "))
array = []
for i in range(n):
    ele = int(input(f"enetr {i} element "))
    array.append(ele)

reverse_array = []    
for i in range(len(array),0,-1):
    reverse_array.append(i)

print("array",array)    
print("Reverse array",reverse_array)    
