# 1
# cal = input()
# counter = 0
# invalid = "no"  

# for i in range(len(cal)):
#     if cal[i] == "(":
#         counter += 1
#     if cal[i] == ")":
#         counter = counter - 1
#         if counter < 0:
#             invalid = "yes"   


# if counter == 0 and invalid == "no":
#     print("درست")
# else:
#     print("نادرست")
#------------------------------

# 2
# n = input("")
# g = n
# e = 0
# h = []
# g = g.split(" ")
# for i in g:
#     e = i
#     if e != "":
#         h.append(i[0])
# h = "".join(h)
# print(h)
#------------------------------
# 3
# a=input()
# b=''
# for i in range (1, len(a)+1 ):
#     b=b+a[-i]
# print(b)
#------------------------------
# 4
# a=input()
# b=''
# for i in range (1, len(a)+1 ):
#     b=b+a[-i]
# if b == a :
#     print('بله')
# else :
#     print('خیر')

#------------------------------
# 5
# a=input()
# b=input()
# n=int(input())
# c=a[:n-1]+b+a[n-1:]
# print(c)
#------------------------------
# 6
# serial_card_number = input("")
# final_list = []
# fin = 0
# for i in range (4):
#     final_list.append(serial_card_number[(4*i):(4*i)+4])
#    # final_list.append("-")
#     #print(final_list)

# print("-".join(final_list))

#------------------------------
# 7
# n=input()
# m=input()
# A=[]
# B=[]
# C=[]
# for i in n:
#     A.append(i)
# for x in m:
#     B.append(x)
# for j in A:
#     if j in B and A.count(j)==B.count(j):
#         C.append('a')
#     else:
#         C.append('b')
# for k in B:
#     if k in A and B.count(k)==A.count(k):
#         C.append('a')
#     else:
#         C.append('b')
# if 'b' not in C:
#     print('Yes!')
# else:
#     print('No!')


#------------------------------
# 1
# a=input()
# b=a
# t=0
# flag = 0
# for i in b :
#     if i == "(" :
#         t+=1
#     if i == ")" :
#         t-=1
#         if t < 0:
#             flag = 1
# if t == 0 and flag == 0 :
#     print("درسته")
# else:
#     print("نادرسته")
#------------------------------    
# 2
# st = input()
# lst = st.split(" ")
# mokhaf = ""
# for i in lst:
#     if i != "":
#         mokhaf = mokhaf + i[0]
# print(mokhaf) 

#------------------------------    
# 3
# kalame=input()
# a=""
# t=-1
# for i in range(len(kalame)):
#     a=a+kalame[t]
#     t=t-1
    
# print(a)
#------------------------------    
# 4
# kalame=input()
# a=""
# t=-1
# for i in range(len(kalame)):
#     a=a+kalame[t]
#     t=t-1
# if a==kalame:
#     print("خوشتیپ است")
# else:
#     print("خوشتیپ نیست")
    
    
#------------------------------    
# 5
# a=input()
# b=input()
# n=int(input())
# c=a[:(n-1)]+ b + a[n-1:]
# print(c)
#------------------------------    
# 6
# s = input()
# r = ""
# i = 0
# while i < len(s):
#     r = r + s[i]
#     i = i + 1
#     if i % 4 == 0 and i != len(s):
#         r = r + "-"
# print(r)
#------------------------------    
# 7
# A = input()
# B = input()
# flag = 1
# for i in A:
#     if A.count(i) != B.count(i):
#         flag = 0
# if flag == 1 and len(A) == len(B):
#     print('yes')
# else:
#     print('no')



