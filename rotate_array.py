no_of_test = int(input())

def rotate(arr):
    for i in range(0,len(arr)-1):
        arr[0],arr[i+1] = arr[i+1],arr[0]
    
    return arr

for i in range(0,no_of_test):
    no_of_elements,rot = map(int, input().split()) 
    arr = [int(x) for x in input().split()]

    for j in range(0,rot):
        arr = rotate(arr)
    
    listToStr = ' '.join(map(str, arr))
    print(listToStr) 
    


        
        

