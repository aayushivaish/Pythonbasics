'''
arr[4,8,6,0,78,123,99,74]

First we will compare each Element with its adjacent element and swap if left > right
And we will repeat this comparison and swapping until the whole array is sorted.
Time Complexity = n^2
'''
def bubble_sort(arr):
    for i in range(0,len(arr)):
        # print("iteration {}".format(i+1))
        flag = 1
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 0
        if flag == 1:
            break 
        # print(arr)
    return arr

arr = [4,8,6,0,78,123,99,74]
sorted_arr = bubble_sort(arr)
print(sorted_arr)