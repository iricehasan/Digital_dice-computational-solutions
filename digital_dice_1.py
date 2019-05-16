import random
permutation_list = []

M = 24 #number of presidents
totalcorrect=0


for k in range(1,1000001):
    correct = 0    
    for i in range(1,25):
        permutation_list.append(i)
        

    random.shuffle(permutation_list)
    term =  permutation_list
    
    for j in range(1,M+1):
        if term[j-1]==j:
            correct += 1
    
    totalcorrect += correct
    
print(float(totalcorrect/1000000))
