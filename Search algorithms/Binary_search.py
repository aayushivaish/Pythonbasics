'''
it is a divide and conquer algorithm

First we will look at middle element

Middle= (low+high)//2 (Median)

We will compare our n with middle index 

arr[mid] == n

if arr[mid] > n

that means the element (n) lies in the first half of an array

if arr[mid] < n

that means the element (n) lies in the second half of an array

We will continue doing this until arr[mid] == n
'''
arr=[2,3,4,5,3,3,9,49,47,90,65,53,1111]
arr.sort()
print(arr)
def binary_search(arr,n,low,high):
    print("low {}".format(low))
    print("high {}".format(high))
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return binary_search(arr,n,low,mid-1)
        elif arr[mid] < n:
            return binary_search(arr,n,mid+1,high)
    else:
        return - 1

ans = binary_search(arr,65,0,len(arr)-1)
if ans != -1:
    print('Element is present at index {} '.format(ans))
else:
    print('Element not found ')
    


