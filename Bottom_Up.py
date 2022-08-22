#Bottom_Up approach
coins = [1,2,5]
coins.sort(reverse=True)
amount = 11
arr = []
for i in range(1,amount+1):
    sum = i
    count=0
    j=0
    while sum>0:
        if sum>=coins[j]:
            sum-=coins[j]
            count+=1
        else:
            j+=1
    arr.append(count)
print(arr[-1])