import random as rd
M = 24
totalcorrect = 0

for k in range(1,1000001):
    correct = 0
    term = list(range(1,M+1))
    for i in range(len(term)):
        term[i] = 0
       
    for j in range(1,M+1):
        term[j-1]=round(rd.uniform(M,0))
        
        
    for i in range(1,M+1):
        if term[i-1]==i:
            correct +=1
                  
        
    totalcorrect += correct
    
print(totalcorrect/1000000)