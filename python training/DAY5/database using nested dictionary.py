n=int(input("enter no of students: "))
m=int(input("enter no of subjects: "))
d={}
for i in range(n):
    k=input("enter the roll no: ")
    v={}
    for j in range(m):
        sub=input("enter the subject name: ")
        marks=int(input("enter marks: "))
        v[sub]=marks
    d[k]=v
for i in d:
    print(i,"-",d[i])

