n = int(input("Size of array "))
array = []
for i in range(n):
    ele = int(input(f"enetr {i} element "))
    array.append(ele)
print("array ",array) 

def reverse(array,i,j):
    while i<=j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    return array    
      
     
print("array ",reverse(array,1,3) )