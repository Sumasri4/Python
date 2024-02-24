n=int(input("enter no of students: "))
m=int(input("enter no of subject: "))
d={}
for i in range(n):
    k=input("enter the roll no: ")
    v={}
    for j in range(m):
        sub=input("enter subject name: ")
        marks=input("enter marks: ")
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i} : {sum{i}/n}")
