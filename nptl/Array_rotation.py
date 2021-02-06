def rotatelist(arr,k):
    j = 0
    while j < k:
        for i in range(0,len(arr)-1):
            arr[0],arr[i+1]=arr[i+1],arr[0]
        j = j+1
    return arr
      
