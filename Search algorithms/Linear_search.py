'''
arr[1,2,3,4,5,6]
# to do
whether a particular element exists or not, if exist then at which position?
'''
def linear_search(arr):
    n=int(input('Enter the element to search '))
    flag=0
    for i in range(0,len(arr)):
        if arr[i] == n:
            print('Element Found at Position {}'.format(i+1))
            flag = 0
            break
        else:
            flag=1
    if flag == 1:
        print('Element Not Found')

arr = [9,4,5,6,7,10,11,111]
linear_search(arr)


