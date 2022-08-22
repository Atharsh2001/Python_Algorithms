coins = [1,2,5,100]
coins.sort(reverse=True)

def SumOfCoin(i,sum):
    if i==len(coins):
        return 0
    if sum>=coins[i]:
        sum-=coins[i]
        print(coins[i],end=" ")
        SumOfCoin(i,sum)
    else:
        i+=1
        SumOfCoin(i,sum)



sum=11
i=0
print(f"Combination of coins needed for {sum} Rupees :")
SumOfCoin(i,sum)