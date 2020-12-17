# to do
'''
[1,2,3,4,5,6,7,8,9,10,11]
if rotate=1
[11,1,2,3,4,5,6,7,8,9,10]
if rotate=2
[10,11,1,2,3,4,5,6,7,8,9]
'''
arr=[1,2,3,4,5,6,7,8,9,10,11]
n=int(input('Enter Rotation '))

def rotate(arr):
    for i in range(0,len(arr)-1):
        arr[0],arr[i+1]=arr[i+1],arr[0]
    return arr

for i in range(0,n):
    arr=rotate(arr)
print(arr)
