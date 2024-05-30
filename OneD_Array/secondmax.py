n = int(input("Enter size of array "))
array = []
for i in range(n):
    ele = int(input("enter elemrnt "))
    array.append(ele)

max = array[0]    
smax = array[0]   

for i in range(len(array)):
    if array[i] > max:
        max = array[i]
    elif array[i] != max and array[i] > smax:
        smax = array[i]    

print(max)
print(smax)