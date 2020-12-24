'''
Select a key Element

Sort Elements according to key Element

Do not swap Elements, instead change the position of key Element

Values of unsorted part are picked and placed at the correct position in the sorted part (like playing cards).

Step 1- Iterate from arr[1] to arr[n]

Step 2- Compare the current Element(key) to its predecessor.

Step 3- If the key Element < its predecessor, then we will compare it to the Element Before and move the greater Element one position up to make space for the key Element.

'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        print("iteration {}".format(i))
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key 
        print(arr)
    return arr 

arr=[9,11,67,34,-11,0,1,87,54,27,18]
ans = insertion_sort(arr)
print(ans)
