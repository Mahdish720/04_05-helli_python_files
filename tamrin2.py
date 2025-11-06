# 2
# Nomre=[18,16,10,11,20,14]
# A=0
# b=0
# for i in Nomre:
#     A=A+i
#     b=b+1
# if A/b>12:
#     print ('"قبول شدید"')
# -------------------
# n=int(input())
# t=0
# names=[]
# for i in range(n):
#     k=input()
#     names.append(k)
#     if k=="ali":
#         t=t+1
        
# print(t)
# -------------------
# adad = [14,17,14,15,25,1019,16,84,147,96]
# adad1 = []
# for i in adad :
#     if i % 2 == 1 :
#         adad1.append(i)
# print(adad1)
# -------------------
# import random
# t=9
# a=[]
# for i in range (10):
#     name=input()
#     a.append(name)
# print(a[random.randint(0,9)])
# for i in range (5):
#     print(a[random.randint(0,9)])
# for i in range (5):
#     akhar=random.randint(0,t)
#     print(a[akhar])
#     del a[akhar]
#     t=t-1
# -------------------
# n=int(input())
# List=[]
# m=0
# for i in range(n):
#     l=int(input())
#     List.append(l)
#     m=m+l
# for i in List:
#     if i>m/n:
#         print(i)
# -------------------
# n = int(input())

# fibonacci_list = []

# if n >= 1:
#     fibonacci_list.append(1)
# if n >= 2:
#     fibonacci_list.append(1)

# for i in range(2, n):
#     next_fib = fibonacci_list[i-1] + fibonacci_list[i-2]
#     fibonacci_list.append(next_fib)

# print(fibonacci_list)
# -------------------



# numbers = []
# for i in range(10):   
#     n = int(input())   
#     numbers.append(n)   
# print(numbers)   
# -------------------
# nomre=[14,20,11,10,16,18]
# j=0
# t=0
# for i in nomre:
#     j=j+i
#     t=t+1
# mian=j/t
# if mian>12:
#     print('قبول شدید')
# -------------------
# ls =[1,2,3,47,8,9,10,2,1]
# nls = []
# for i in ls :
#     if i % 2 == 1:
#         nls.append(i)
# print(nls)
# -------------------
# import random
# A = []
# for i in range(10) :
#     name = input()
#     A.append(name)
# print("part 1 :")
# r = random.randint(0 , 9)
# print(A[r])
# print("part 2 :")
# for i in range(5):
#     r = random.randint(0 , 9)
#     print(A[r])
# print("part 3 :")
# k = 9
# for i in range(5):
#     r = random.randint(0 , k)
#     print(A[r])
#     del A[r]
#     k = k - 1
# -------------------
# n=int(input())
# y=0
# adad=[]
# maj=0
# for i in range(n):
#     x=int(input())
#     y=y+1
#     maj=maj + x
#     adad.append(x)
# mianginkol=maj/y
# for j in adad :
#     if j > mianginkol:
#         print(j)
# -------------------

# l1 = [1,1]
# n =  int(input())
# # 0 dorost nashod
# if n == 1:
#     print([1])
# else:
#     for i in range(n-2):
#         a =  l1[-1] + l1[-2]
#         l1.append(a)
#     print(l1)

