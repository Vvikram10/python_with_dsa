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

k = int(input("Enter time of rotate "))

def rotate(array,k) :
    m = len(array) 
    k = k % m
    if k > 0:
        reverse(array,0,m-k-1)
        reverse(array,m-k,m-1)
        reverse(array,0,m-1)
    return array     

      
    
print("array ",rotate(array,k) )