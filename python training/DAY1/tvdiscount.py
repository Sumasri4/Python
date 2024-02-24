a,b,c,d=map(int,input().split(" "))
x=a-(a*c/100)
y=b-(b*d/100)
if x==y:
    print("any")
elif x<y:
    print("first")
else:
    print("second")

