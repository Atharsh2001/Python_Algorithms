from itertools import combinations_with_replacement as perm
sum1 = 11
coins = [1,2,5]
lis = []
for i in range(1,sum1+1):
    lis.append(perm(coins,i))
temp = []
for i in lis:
    for j in i:
        if sum(j)==sum1:
            temp.append(j)
print(f"Combination of coins needed for {sum1} Rupees :")
print(*temp[0])
