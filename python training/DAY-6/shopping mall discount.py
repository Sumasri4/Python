#shopping mall having 5%discount for men and 7% discount for women and individually discount for each item they purchase is 3*numberr of items they purhase calculate the total bill.
n=int(input("enter no of items: "))
d={}
for i in range(n):
    key = input("items: ")
    value = int(input("price: "))
    d[key] = value
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter gemnder: ")
if g == "male":
     bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items - price : discount-price")
for i in d:
    print(f"{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"total bill:{bill}")
    
   
