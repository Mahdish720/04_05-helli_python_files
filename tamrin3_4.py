# n = int(input())
# my_list = []
# for i in range(n):
#     my_list.append(i+1)
    
# def badi(lst , shoroo):
#     new_lst = []
#     for i in range(shoroo,len(lst)):
#         if shoroo % 2 == i % 2 :
#             new_lst.append(lst[i])
#             if i == len(lst) - 1:
#                 new_lst.append('yes')
#     return new_lst

# shoroo = 1
# print(my_list)
# while len(my_list) != 1 :
#     my_list = badi(my_list,shoroo)
#     if my_list[-1] == 'yes':
#         shoroo = 1
#         del my_list[-1]
#     else:
#         shoroo = 0
#     print(my_list)

# print([])


mylist = [1,2,3,4,5]
for i in range(len(mylist)):
    for j in range(i,len(mylist)):
        t = []
        for k in range(i,j+1):
            t.append(mylist[k])
        print(t)

# n = int(input())
# list = []
# for i in range(n):
#     a = int(input())
#     list.append(a)
# x = []
# y = []
# for i in range(n):
#     a = list[i]
#     b = 0
#     for j in range(n):
#         if list[j] == a:
#             b += 1
#     x.append(b)
#     y.append(a)
# b = -1
# for i in range(n):
#     if x[i] > b:
#         b = x[i]
#         a = y[i]
# print(a)


# n=int(input())
# t=0
# l=[]
# for i in range(n):
#     s=int(input())
#     l.append(s)
# for j in l:
#     r=l.count(j)
#     if r > t:
#         t=r
#         m = j
# print(m)
# --------------
# n=int(input())
# test=[]
# test1=[]
# for i in range(n):
#     x= int(input())
#     if x%2==0:
#         test1.append(x)
#     else:
#         test.append(x)
# test.extend(test1)
# print(test)
# --------------
# ml=[]
# ml2=[]
# ml3=[]
# for i in range(5):
#     esm=input()
#     ml.append(esm)
# for y in range(20):
#     ray=input()
#     ml2.append(ray)
# for u in range(5):
#     p=ml2.count(ml[u])
#     ml3.append(ml[u])
#     ml3.append(p)
# print(ml3)
# --------------
# hame ro be tartib nadim
# def function_max(A):
#     a=A[0]
#     for i in range(1,len(A)):
#         if A[i]>a:
#             a=A[i]
#     return a
# n=int(input())
# List=[]
# for i in range(n):
#     List.append(int(input()))
# for i in range(n//2):
#     List.remove(function_max(List))
# print(function_max(List))
# --------------
# n = int(input(""))
# A = []
# B = []
# num = []
# for i in range(n):
#     h = int(input(""))
#     A.append(h)
# k = int(input(""))
# for j in range(k):
#     f = int(input(""))
#     B.append(f)
# while len(A) != 0 and len(B) != 0:
#     if A[0] < B[0]:
#         num.append(A[0])
#         del A[0]
#     else:
#         if A[0] > B[0]:
#             num.append(B[0])
#             del B[0]
#         else:
#             num.append(A[0])
#             num.append(B[0])
#             del A[0]
#             del B[0]
# num.extend(A)
# num.extend(B)
            
# print(num)


n=int(input())
A=[]
for i in range(2,n):
    a=0
    for j in A:
        if i%j==0:
            a=a+1
    if a==0:
        A.append(i)
print(A)
    



    

