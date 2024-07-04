
a=int(input("num"))
temp=a
sum=0
d=temp%10
while(temp>0):
    d=temp%10
    if(d%2==0):
        sum=sum+d
        temp=temp//10
    else:
        sum=sum+0
        temp=temp//10

    
print(sum)
