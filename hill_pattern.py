for i in range(1,6):
    for k in range(5,i,-1):
        print(end="  ")
    for j in range(1,i+1):
        print(j,end="   ")
        
    print()    

#         1   
#       1   2   
#     1   2   3   
#   1   2   3   4   
# 1   2   3   4   5   

# --------------------------------------

for i in range(1,6):
    for k in range(5,i,-1):
        print(end="  ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i+1,i*2):
        print(j,end=" ")    
    print()

#         1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9 

# --------------------------------------

for i in range(1,6):
    for k in range(5,i,-1):
        print(end="  ")
    for j in range(1,i+1):
        print(i,end=" ")
    for j in range(i+1,i*2):
        print(i,end=" ")    
    print() 

#         1 
#       2 2 2 
#     3 3 3 3 3 
#   4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 

# --------------------------------------

for i in range(1,6):
    for k in range(5,i,-1):
        print(end="  ")
    for j in range((i*2-1),i-1,-1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")    
    print() 

#         1 
#       3 2 1 
#     5 4 3 2 1 
#   7 6 5 4 3 2 1 
# 9 8 7 6 5 4 3 2 1 

# --------------------------------------

for i in range(1,6):
    for k in range(5,i,-1):
        print(end="  ")
    for j in range(i,i*2):
        print(j,end=" ")
    for j in range(i*2-2,i-1,-1):
        print(j,end=" ")    
    print()

#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 

# --------------------------------------