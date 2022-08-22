elements = ['a','b','c','','e','f','g','h','i','j','k']
count1= 1
n=len(elements)
i=0
while(elements.count('-')<n-1):
    if i==n:
        i=0
    if elements[i]!='-':
        if count1%5==0 or count1%10==5:
            count1+=1
            elements[i]='-' 
        if elements[i]!='-':
            count1+=1
    i+=1
for j in elements:
    if j!='-':
        print(f"The Winner Element is ->  '{j}'")