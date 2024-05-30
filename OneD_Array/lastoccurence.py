n = int(input("Size of array "))
array = []
for i in range(n):
    ele = int(input(f"enetr {i} element "))
    array.append(ele)

key = int(input("Enter the no find lastoccurence "))

for i in range(len(array)-1,-1,-1):
    if array[i] == key :
        print("no is ",i)
        break
    else:
        print("no is not present ")

        