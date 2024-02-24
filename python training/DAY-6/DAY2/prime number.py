a=int(input("enter a number"))
count=0
for i in range(1,a+1):
    if a%i==0:
        print(i)
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")




'''a=int(input("enter a number"))
   count=0
   for i in range(1,a+1):
      if a%i==0:
        print(i)
        count+=1
   if count==2:
       print("prime")
   else:
       print("not a prime")'''


'''a=int(input("enter a number"))
    for i in range(2,a):
      if a%i==0:
       print(" not a prime")
       break
    else:
       print("prime")'''



'''a=int(input("enter a number"))
    for i in range(2,(a//2)+1):
      if a%i==0:
       print(" not a prime")
       break
    else:
       print("prime")'''


'''a=int(input("enter a number"))
    for i in range(2,(a**0.5)+1):
      if a%i==0:
       print(" not a prime")
       break
    else:
       print("prime")'''


'''a=int(input("enter a number"))
   i=2
   while i < (a**0.5)+1):
      if a%i==0:
       print(" not a prime")
       break
       i+=1
    else:
       print("prime")
   




