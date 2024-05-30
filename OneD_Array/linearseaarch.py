print("Enter size of array")
n = int(input("size is "))

array = []

for i in range(n):
    ele = int(input("enter element "))
    array.append(ele)

key = int(input("find element "))

if key in array:
    print("no is present at index", array.index(key))
else:
    print("no not found")


