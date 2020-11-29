def isPrime(n):
    loopVar = n-1
    flag = 0
    while(loopVar > 1):
        if n % loopVar == 0:
            flag = 1
            break
        else:
            flag - 0
        loopVar = loopVar -1
    return flag


arr =  [9,11,12,45,2,13,43,24]

def main(arr):
    for i in range(0,len(arr)):
        if isPrime(arr[i]) == 0:
            print("{} is a Prime Number".format(arr[i]))
        else:
            print("{} is not a Prime Number".format(arr[i]))

main(arr)