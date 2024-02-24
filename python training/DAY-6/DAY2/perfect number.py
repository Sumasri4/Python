a=int(input())
count=0
for i in range(1,a):
    if a%i==0:
        print(i)
        count+=i
if count==a:
    print("perfect number")
else:
    print("not a perfect number")
