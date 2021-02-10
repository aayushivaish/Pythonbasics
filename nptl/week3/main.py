def remdup(arr):
    final_arr = []
    
    for i in arr:
        if i in final_arr:
            final_arr.remove(i)
            final_arr.append(i)
        else:
            final_arr.append(i)
    return final_arr

############################

def splitsum(l):
    sum,cube = 0,0
    for i in l:
        if i > 0:
            sum = sum + i**2
        else:
            cube = cube + i ** 3
    
    return [sum,cube]

######################################

def matrixflip(m,d):
    if d == 'h':
        final_matrix = [list(row) for row in m]
        for i in final_matrix:
            i.reverse()
    elif d == 'v':
        final_matrix = m.copy()
        final_matrix.reverse()
    
    else:
        return final_matrix
        
    
    return final_matrix
