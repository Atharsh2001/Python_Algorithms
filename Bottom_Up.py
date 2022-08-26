#Bottom_Up approach
from itertools import combinations_with_replacement as com
coins = [1,2,5]
amount = 11
arr = [0]*(amount+1)
for i in range(1,amount+1):
    if i in coins:
        arr[i]=1
    else:
        lis = [k for k in range(1,i)]
        ans = []
        for j in range(1,i+1):
            t = list(com(lis,j))
            for j in t:
                if sum(j)==i:
                    _=[]
                    for i1 in j:
                        _.append(arr[i1])
                    ans.append(sum(_))
        arr[i]=min(ans)
print(arr)
