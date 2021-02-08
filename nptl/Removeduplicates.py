def remdup(arr):
    final_arr= []
    for i in range(0,len(arr)):
        ro = False
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                ro = True
               #arr.remove(arr[i])
        if ro == False:
            
            final_arr.append (arr[i])
    return final_arr
print (remdup([3,1,3,5]))
print (remdup([7,3,-1,-5]))
print (remdup([3,5,7,5,3,7,10]))
