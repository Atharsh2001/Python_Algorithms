queens = 4
chess = [[0 for i in range(queens)] for j in range(queens)]
def is_attack(i, j):
    for k in range(0,queens):
        if chess[i][k]==1 or chess[k][j]==1:
            return True
    for k in range(0,queens):
        for l in range(0,queens):
            if (k+l==i+j) or (k-l==i-j):
                if chess[k][l]==1:
                    return True
    return False

def N_queen(n):
    if n==0:
        return True
    for i in range(0,queens):
        for j in range(0,queens):
            if (not(is_attack(i,j))) and (chess[i][j]!=1):
                chess[i][j] = 1
                if N_queen(n-1)==True:
                    return True
                chess[i][j] = 0

    return False

N_queen(queens)
print("The queen placement are :")
print(*chess,sep='\n')