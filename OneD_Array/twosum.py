n = int(input("Size of array "))
array = []
for i in range(n):
    ele = int(input(f"enetr {i} element "))
    array.append(ele)

key = int(input("Enter the no find addtion "))    

for i in range(len(array)-2):
    for j in range(len(array)-1):
        if array[i] + array[j] ==  key:
            print(f'total no of addtion ({i} {j})')   