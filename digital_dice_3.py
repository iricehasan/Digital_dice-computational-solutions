import random as rd
S = 0
L = 1
r = [1,1,1,1,1,1]
for i in range(1,1000001):
    for j in range(1,4):
        r[j-1] = rd.random() #x values
    for j in range(4,7):
        r[j-1] = L*rd.random() #y values

    """ 
    a^2 = b^2 + c^2 - 2*b*c*cos(A)        cos(A) = ((b^2+c^2)-a^2)/(2*b*c)
    b^2 = a^2 + c^2 - 2*a*c*cos(B)        cos(B) = ((a^2+c^2)-b^2)/(2*a*c)   
    c^2 = a^2 + b^2 - 2*a*b*cos(C)        cos(C) = ((a^2+b^2)-c^2)/(2*a*b)   
    """
    #if pi/2<x<pi , cos(x) ---> negative

    a_sqr = (r[0]-r[1])**2+(r[3]-r[4])**2
    b_sqr = (r[1]-r[2])**2+(r[4]-r[5])**2    
    c_sqr = (r[0]-r[2])**2+(r[3]-r[5])**2
    
    if a_sqr < b_sqr + c_sqr and b_sqr < c_sqr+a_sqr and c_sqr < a_sqr + b_sqr:
        obtusetriangle = 0
    else:
        obtusetriangle = 1

    S += obtusetriangle
print(S/1000000)
    
