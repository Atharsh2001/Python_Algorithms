amount = 11
coins = [1,2,5]
ans = []
while(amount>0):
    temp = []
    for i in coins:
        t = amount-i
        if t>=0:
            temp.append(amount-i)
    mini = temp.index(min(temp))
    ans.append(coins[mini])
    amount=temp[mini]
print(ans)