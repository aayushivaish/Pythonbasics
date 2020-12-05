import math

def taylor_sin_x(x,n):
    check = 0
    
    ans = 0
    for i in range(0,n):
        check = ans
        coefficient = (i*2)+1
        sign = (-1)**(i)
        
        num = x**coefficient
        den = math.factorial(coefficient)
        ans = ans + (sign)*(num/den)
        ans = round(ans,2)
        
        
        if(ans == check):
            break
        
       
    
    return ans 

angle_rad = (math.radians(360))
x = taylor_sin_x(angle_rad,15)
print(x)
