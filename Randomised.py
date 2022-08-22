import random
coins = [1,2,5]
amount = 11
i=0
print(f"The random combinations needed for {amount} Rupees : ")
while(amount>0):
    ran = random.choice(coins)
    if (amount-ran)<0:
        continue
    amount-=ran
    print(ran,end=" ")
    