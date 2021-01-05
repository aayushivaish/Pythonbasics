def pallindrome(n):
    loopVar = n
    rev = 0
    while(loopVar != 0):
        last = loopVar % 10
        rev = rev*10+last
        loopVar = loopVar // 10
    return rev,if_pallindrome(n,rev)
    
    
def if_pallindrome(n,rev):
    if n == rev:
        return True
    else:
        return False

ans,is_pal = pallindrome(121)

print(ans) #pallindrome result
print(is_pal) # to check if the number is pallindrome
