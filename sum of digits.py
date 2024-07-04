#sum of didits
a=int(input("num"))
temp=a
sum=0
d=temp%10
while(temp>0):
    d=temp%10
    sum=sum+d
    temp=temp//10

print(sum)    
