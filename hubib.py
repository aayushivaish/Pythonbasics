def rotatelist(l,k):
    p = l[:]
    for i in range(k):
        rotate(p)
    return p
        
    # print(r,l)

def rotate(l):
    for i in range(0,len(l)-1):
        l[i],l[i+1] = l[i+1],l[i] 
