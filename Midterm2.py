# # 1. 
# n = int(input())
# all = []
# for i in range(n):
#     temp = int(input())
#     all.append(temp)

# out_lst = []
# t = 0

# for i in all:
#     if i != 0 :
#         out_lst.append(i)
#     else:
#         t = t + 1
        
# for i in range(t):
#     out_lst.append(0)
    
# print(out_lst)

# ----------------
# 2.
# jomle = input() # faghat horoof kochak englisi hastan...
# n = int(input())
# out = ''

# for i in jomle:
    
#     temp = ord(i) + n
    
#     # age ba n mosbat biroon zad
#     if temp > ord('z'):
#         temp = (temp - ord('z')) % ( ord('z') - ord('a') + 1 ) + ord('a') - 1
    
#     # age ba n manfi biroon zad
#     if temp < ord('a'):
#         temp = ord('z') - (ord('a') - temp) % ( ord('z') - ord('a') + 1 ) + 1 
    
#     out = out + chr(temp)
    
# print(out)     
        
# ----------------
# 3.
# import pygame
# import time

# pygame.init()

# img = pygame.image.load("32.png")
# img_w , img_h = img.get_size()

# screen = pygame.display.set_mode((img_w,img_h))

# for i in range(img_w):
#     for j in range(img_h):
        
#         r,g,b,a = img.get_at((i,j))
#         mean = (r + g + b) / 3
#         color = 0
#         if mean > 127.5 :
#             color = 255
#         else:
#             color = 0
            
#         img.set_at((i,j),(color, color, color))

# screen.blit(img,(0,0))
# pygame.display.update()

# time.sleep(3)

# ----------------
# 4.alef

# def check(lst , i , j):
#     t = 0
#     if lst[i][j-1] == 1:
#         t = t + 1
#     if lst[i][j+1] == 1:
#         t = t + 1
#     if lst[i-1][j] == 1:
#         t = t + 1
#     if lst[i+1][j] == 1:
#         t = t + 1
    
#     if t >= 2 :
#         return 'Yes'
#     else:
#         return 'No'
    
# def hazf(lst):
#     lst2 = []
#     for i in range(n):
#         temp = []
#         for j in range(n):
#             temp.append(lst[i+1][j+1])
#         lst2.append(temp)
#     return lst2
    

# def lst_copy(lst):
#     lst2 = []
#     for i in range(len(lst)):
#         temp = []
#         for j in range(len(lst)):
#             temp.append(lst[i][j])
#         lst2.append(temp)

#     return lst2


# n = int(input())

# lst = []

# temp = []
# for i in range(n+2):
#     temp.append(0)
# lst.append(temp)


# for i in range(n):
#     temp = []
#     temp.append(0)
#     for j in range(n):
#         temp.append(int(input()))
#     temp.append(0)
#     lst.append(temp)

# temp = []
# for i in range(n+2):
#     temp.append(0)
# lst.append(temp)

# lst_temp = lst_copy(lst)

# for i in range(n):
#     for j in range(n):
#         if check(lst,i+1,j+1) == 'Yes':
#             lst_temp[i+1][j+1] = 1

# print(hazf(lst_temp))


# ------------
# 4.b

# # check kardan inke hame virusi shodan ya na
# def check_all(lst, n):
#     t = 'Yes'
    
#     for i in range(n):
#         for j in range(n):
#             if lst[i+1][j+1] != 1:
#                 t = 'No'
    
#     return t

# # check kardan inke yek khoone virusi mishe ya na
# def check(lst , i , j):
#     t = 0
#     if lst[i][j-1] == 1:
#         t = t + 1
#     if lst[i][j+1] == 1:
#         t = t + 1
#     if lst[i-1][j] == 1:
#         t = t + 1
#     if lst[i+1][j] == 1:
#         t = t + 1
    
#     if t >= 2 :
#         return 'Yes'
#     else:
#         return 'No'

# # hazf kardan satr o sotoone 0 ezafi ke khodemoon add kardim
# def hazf(lst):
#     lst2 = []
#     for i in range(n):
#         temp = []
#         for j in range(n):
#             temp.append(lst[i+1][j+1])
#         lst2.append(temp)
#     return lst2
    

# # yek copy az list bar migardoone
# def lst_copy(lst):
#     lst2 = []
#     for i in range(len(lst)):
#         temp = []
#         for j in range(len(lst)):
#             temp.append(lst[i][j])
#         lst2.append(temp)

#     return lst2


# n = int(input())

# lst = []

# # yek satr ezafe 0 aval gharar midam ke error out of range nakhoram
# temp = []
# for i in range(n+2):
#     temp.append(0)
# lst.append(temp)


# for i in range(n):
#     temp = []
#     # yek sotoone 0 avav ezafe gharar midam ke out of range nakhoram
#     temp.append(0)
#     for j in range(n):
#         temp.append(int(input()))
    
#     # yek sotoone 0 akhar gharar midam ke out of range nakhoram
#     temp.append(0)
#     lst.append(temp)

# # yek satr akhar 0 gharar midam ke out of range nakhoram
# temp = []
# for i in range(n+2):
#     temp.append(0)
# lst.append(temp)

# # marhale badi ro mohasebe mikonam va dar lst_temp gharar midam
# lst_temp = lst_copy(lst)
# for i in range(n):
#     for j in range(n):
#         if check(lst,i+1,j+1) == 'Yes':
#             lst_temp[i+1][j+1] = 1
            
# # t hesab mikone chand sanie ast
# t = 0
# while lst_temp != lst :
#     lst = lst_copy(lst_temp) 
#     t = t + 1
#     for i in range(n):
#         for j in range(n):
#             if check(lst,i+1,j+1) == 'Yes':
#                 lst_temp[i+1][j+1] = 1

# print(hazf(lst_temp))
# print(check_all(lst_temp , n))
# if check_all(lst_temp,n) == 'Yes':
#     print(t)


