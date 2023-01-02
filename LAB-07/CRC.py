def copy(arr):
    arr_copy=[]
    for i in range(0, len(arr)):
        arr_copy.append(arr[i])
    return arr_copy
   
def crc(key, dataword):
    key_copy = key
    dataword_copy = dataword
    for i in range(0, len(key)-1):
        dataword_copy.append(0)
    print(dataword_copy)
   
    n=len(key)
    print(n)
    arr=[]
    for i in range(0,n):
        arr.append(dataword_copy[i]^key[i])
   
    arr_copy= arr
   
    for i in range(n+1,len(dataword_copy)):
        arr_copy.pop(0)  
        arr_copy.append(dataword_copy[i])
        if arr_copy[0]==1:
            arr= copy(arr_copy)
            arr_copy.clear()
            for j in range(0,n):
                arr_copy.append(arr[j]^key[j])
           
        else:
            arr= copy(arr_copy)
            arr_copy.clear()
            for k in range(0,n):
                arr_copy.append(arr[k]^0)
           
    arr_copy.pop(0)
    return arr_copy


key= [1,1,0,1]
dataword=[1,0,0,1,0,0]
code= []
code.append(crc(key, dataword))
print(code)

