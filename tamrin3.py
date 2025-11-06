# n = int(input())
# z=0
# x=0
# nomre=[]
# nomre2=[]
# for i in range(n):
#     a = float(input())
#     nomre.append(a)
#     nomre2.append(a)
# for i in range(n):
#     z=z+nomre[i]
# ort=z/n
# for i in range(n):
#     if nomre2[i]==ort:
#         print(i+1)
#     else:
#         x=x+1
# if x==n:
#     print("hich!")
# ---------------
# n = int(input())

# numbers = []


# for i in range(n - 1):
#     numbers.append(int(input()))


# for i in range(1, n+1):
#     if i not in numbers:
#         print(i)
# ---------------
# n = int(input(""))
# grades = []
# num=0
# for i in range (n):
#     num = int(input(""))
#     if num not in grades:
#         grades.append(num)
# print(grades)
# ---------------
# a = []
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# b = []
# b.append(a[n-2])
# b.append(a[n-1])
# for j in range(2, n):
#     b.append(a[j-2])
# print(b)
# ---------------
# n=int(input())
# x=int(input()) % n
# x_m=-x
# a=[]
# b=[]
# for i in range(n):
#     adad=int(input())
#     a.append(adad)
# for j in range(n):
#     b.append(a[x_m])
#     x_m=x_m+1
# print(b)
# ---------------
# n=int(input())
# people=[]
# i=1
# while i<=n:
#     people.append(i)
#     i=i+1
# kill_next=1
# while len(people)>1:
#     print(people)
#     survivors=[]
#     k=kill_next
#     j=0
#     while j<len(people):
#         if k==0:
#             survivors.append(people[j])
#         k=1-k
#         j=j+1
#     if len(people)%2==1:
#         kill_next=1-kill_next
#     people=survivors
# print(people)
# print([])


# ---------------
# n = int(input())
# nomre = []
# for i in range(n):
#     x = float(input())
#     nomre.append(x)
# jam = 0
# for i in range(n):
#     jam = jam + nomre[i]
# avg = jam / n
# p = 0
# for i in range(n):
#     if nomre[i] == avg:
#         print(i+1)
#         p= 1
# if p == 0:
#     print("hich!")
# ---------------
# n=int(input())
# myList=[]
# for i in range(n-1):
#     x=int(input())
#     myList.append(x)
# for j in range(1,n+1):
#     if j not in myList:
#         print(j)
# ---------------
# n=int(input())
# p=[]
# o=[]
# for i in range(n):
#     m=int(input())
#     p.append(m)
# for i in p:
#     if i not in o:
#         o.append(i)
# print(o)
# ---------------
# n = int(input())
# a = []
# b = []
# for i in range(n):
#     x = int(input())
#     b.append(x)
# a.append(b[-2])
# a.append(b[-1])
# for i in range(n-2):
#     a.append(b[i])
# print(a)
# ---------------
# n = int(input())
# x = int(input())
# a = []
# if n != 0:
#     for i in range(n):
#         p = int(input())
#         a.append(p)
#     x = x%n
#     for i in range(n-x):
#         a.append(a[0])
#         del a[0]
#     print(a)
# ---------------
# n=int(input())
# list=[]
# for i in range(1,n+1):
#     list.append(i)

# def zoj(list):
#     re=[list[0]]
#     for i in range(1,len(list)):
#         if i%2==0:
#             re.append(list[i])
#     if len(list)!=1:
#         if i%2==0:
#             re.append(i)
#         else:
#             re.append(i-1)

#     return re
# def fard(list):
#     re=[]
#     for i in range(1,len(list)):
#         if i%2==1:
#             re.append(list[i])
#     if len(list)!=1:
#         if i%2==1:
#             re.append(i)
#         else:
#             re.append(i-1)
#     return re
# def copy(list):
#     re=[]
#     for i in list:
#         re.append(i)
#     return re
# a=[]
# c=0
# t=0
# while list!=a:
#     print(list)
#     b=len(list)-1
#     if c==0:
#         list2=fard(list)
#         if len(list2)>0:
#             d=list2[-1]
#             del list2[-1]
#     else:
#         list2=zoj(list)
#         if len(list2)>0:
#             d=list2[-1]
#             del list2[-1]
#     c=b-d
#     list=copy(list2)
# print(a)


# ---------------
# n=int(input())
# mylist=[]
# for i in range(1,n+1):
#     mylist.append(i)

# def f(lst,shoroo):
#     new = []
#     for i in range(shoroo ,len(lst)):
#         if i % 2 == shoroo % 2:
#             new.append(lst[i])
#             if i == len(lst) - 1 :
#                 new.append("yes")

#     return new

# print(mylist)
# shoroo = 1
# while len(mylist) != 1 :
#     mylist = f(mylist,shoroo)
#     if mylist[-1] == 'yes':
#         shoroo = 1
#         del mylist[-1]
#     else:
#         shoroo = 0
#     print(mylist)
# print([])

a = [25, 25, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
print(len(a))
