import numpy as np
import math
import itertools
def read_lr(n):
    f = open("lr" + str(n) +".txt", "r")
    lr = [line.replace( '"', "") for line in f.readlines()]    
    lr = [line.replace( "'", "") for line in lr] 
    lr = [line.replace("\n", "") for line in lr]
    lr = [line.replace("[", "") for line in lr]
    lr = [line.replace("]", "") for line in lr]
    lr = [np.fromstring(line,dtype=int,sep=',').reshape(n,n) for line in lr]
    return lr

def number_of_latine_squares(lr,n):
    return len(lr) * math.factorial(n) * math.factorial(n-1) 

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a
    
def reduceLS(LS):
    percol = LS[0,:].argsort()
    LQ = LS[:,percol]
    perrow = LQ[:,0].argsort() 
    LR = LQ[perrow,:]
    return LR

def generate_LR_from_rows_and_colum(LS,n):
    S=set()
    for i in range(n):
        percol = LS[i,:].argsort()
        LQ = LS[:,percol]
        perrow = LQ[:,0].argsort() 
        LR = LQ[perrow,:]
        S.add(totuple(LR))
    for i in range(n):
        perrow = LS[:,i].argsort()
        LQ = LS[perrow,:]
        percol = LQ[0,:].argsort() 
        LR = LQ[:,percol]
        S.add(totuple(LR))
    return S

def permutate_entries(LR,per):
    
    return np.array([[per[x-1] for x in  row] for row in LR])
    

def generate_from_LR(LR,n):
    Z = set()
    S_n= list(itertools.permutations(range(1,n+1)))
    for s in S_n:
        L_per = permutate_entries(LR,s)
        Z = Z | generate_LR_from_rows_and_colum(L_per,n)
    return Z
    
def make_set_of_lr(lr):
    return {totuple(A) for A in lr}

def count_numbers_of_izotopy_class(lr,n):
    I=[]
    set_of_lr = make_set_of_lr(lr)
    set_of_lr.pop
    while set_of_lr :
        x = set_of_lr.pop()
        s = generate_from_LR(x,n)
        I.append(s)
        set_of_lr = set_of_lr - s
    return len(I)

if __name__=="__main__":
    
    lr4 = read_lr(4)
    lr5 = read_lr(5)
    lr6 = read_lr(6)
    print("I(LS(4)) =",count_numbers_of_izotopy_class(lr4,4))
    print("I(LS(5)) =",count_numbers_of_izotopy_class(lr5,5))
    print("I(LS(6)) =",count_numbers_of_izotopy_class(lr6,6))
    
    
    