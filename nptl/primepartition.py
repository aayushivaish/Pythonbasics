def primepartition(m):
    prime_numbers = list_prime(m)
    for i in prime_numbers:
        is_sum = False
        for j in prime_numbers:
            if i+j == m:
                is_sum = True
                return is_sum
            if i+j > m:
                break
    return is_sum
    
    
    

def list_prime(m):
    prime_list = []
    for i in range(2,m):
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            prime_list.append(i)
    return prime_list
                
