coins = [1,2,5,100,200]
coins.sort(reverse=True)
i=0
sum = 11
print(f"Combination of coins needed for {sum} Rupees :")
while(sum>0):
    if sum>=coins[i]:
        sum-=coins[i]
        print(coins[i],end=" ")
    else:
        i+=1