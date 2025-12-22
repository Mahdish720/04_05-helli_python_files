# 1.handle nakarde \n akhar
# a=open("avali.txt","r")
# d=open("dovomi.txt","w")
# c = a.readlines()
   
# for i in c:
#     if i!="\n":
#         d.write(i)

# a.close()
# d.close()


# 1 ba handle kardan \n akhar

# a=open("avali.txt","r")
# d=open("dovomi.txt","w")
# c = a.readlines()

# c_por = []
# for i in c:
#     if i != '\n':
#         c_por.append(i)
   
# for i in range(len(c_por)):
#     if i != len(c_por)-1:
#         d.write(c_por[i])
        
# if "\n" not in c_por[-1]:
#     d.write(c_por[-1])
# else:
#     jomle = c_por[-1]
#     d.write(jomle[:-1])
#     # print(len(jomle),jomle[:-1],jomle[:-2]) baraye test \n
#     # print(jomle[-1])

# a.close()
# d.close()


######
# #2
# def mystr(a):
#     result = ''
#     adad = '0123456789'
#     123
#     23
#     while a != 0 :
#         b = a % 10
#         result = adad[b] + result
#         a = a // 10
#     return result
    
# f = open("ostad.txt", "r")
# text = f.readlines()
# f.close()
# f = open("shagerd.txt", "a")
# for i in range(len(text)):
#     f.write(mystr(i+1)+". "+text[i]) 
# f.close()

# 3.
# myfile = open("/home/mahdi/Desktop/helli/04_05/codes/golabi.txt",'r')
# matn = myfile.read()
# myfile.close()

# sedadar = "aAeEoOiIuU"
# nahayi = ""
# myfile2 = open("/home/mahdi/Desktop/helli/04_05/codes/glb.txt",'w')
# for i in matn:
#     if i not in sedadar:
#         nahayi = nahayi + i

# myfile2.write(nahayi)
# myfile2.close()

# 4 salam -> bye : salamati -> byeati 
# old = input()
# new = input()
# f = open('sib.txt', 'r')
# text = f.read()
# f.close()
# text = text.split(old)
# text = new.join(text)
# f = open('moz.txt', 'w')
# f.write(text)
# f.close()

# 4 salam -> bye : salamati -> salamati
# a=input()
# b=input()
# f=open("sib.txt","r")
# text=f.readlines()
# for i in range(len(text)):
#     zir_text = text[i].split(" ")
#     for j in range(len(zir_text)):
#         if zir_text[j]==a:
#             zir_text[j]=b
#         if zir_text[j]==a+'\n':
#             zir_text[j]=b+'\n'
#     text[i] = " ".join(zir_text)
# text="".join(text)
# f1=open("moz.txt","w")
# f1.write(text)
# f1.close()
# f.close()

# # 5.
# myfile = open("/home/mahdi/Desktop/helli/04_05/codes/yek.txt", "r")
# lines1 = myfile.readlines()
# myfile.close()

# file2 = open("/home/mahdi/Desktop/helli/04_05/codes/do.txt", "r")
# lines2 = file2.readlines()
# file2.close()

# file3 = open("/home/mahdi/Desktop/helli/04_05/codes/se.txt", "w")

# if len(lines1) >= len(lines2):
#     max_length = len(lines1)
# else:
#     max_length = len(lines2)

# for i in range(max_length):
#     if i < len(lines1):
#         if i == len(lines1) - 1 and '\n' not in lines1[i]:
#             file3.write(lines1[i] + '\n')
#         else: 
#             file3.write(lines1[i])
#     if i < len(lines2): 
#         if i == len(lines2) - 1 and '\n' not in lines2[i]:
#             file3.write(lines2[i] + '\n')
#         else: 
#             file3.write(lines2[i])

# file3.close()

# 6
# file1 = open("/home/mahdi/Desktop/helli/04_05/codes/bozorg.txt", "r")
# lines = file1.readlines()
# file1.close()

# shomare_qesmat = 1
# shomare_khat = 0

# name_file = "/home/mahdi/Desktop/helli/04_05/codes/qesmate" + str(shomare_qesmat) + ".txt"
# myfile = open(name_file, "w")


# for line in lines:
#     if shomare_khat < 10:
#         myfile.write(line)
#         shomare_khat = shomare_khat + 1
#     else:
        
#         myfile.close()
#         shomare_qesmat = shomare_qesmat + 1
#         name_file = "/home/mahdi/Desktop/helli/04_05/codes/qesmate" + str(shomare_qesmat) + ".txt"
#         myfile = open(name_file, "w")
#         myfile.write(line)
#         shomare_khat = 1  

# myfile.close()


# 7
# myfile = open("/home/mahdi/Desktop/helli/04_05/codes/namoratab.txt", "r")
# lines = myfile.readlines()
# myfile.close()

# for i in range(len(lines)):
#     for j in range(0, len(lines) - i - 1):
#         if len(lines[j]) > len(lines[j+1]):  
#             temp = lines[j]
#             lines[j] = lines[j+1]
#             lines[j+1] = temp

# file2 = open("/home/mahdi/Desktop/helli/04_05/codes/moratab.txt", "w")
# for line in lines:
#     file2.write(line)
# file2.close()

# ---------------------
# s=0
# a=open('avali.txt','r')
# lines1=a.readlines()
# print(lines1)
# s=open('dovomi.txt','w')
# for i in range(len(lines1)):
#     if (lines1[i]!='\n'):
#         s.write(lines1[i])

# a.close()
# s.close()
# -----------

# def ad(n):
#     list=["0","1","2","3","4","5","6","7","8","9"]
#     a=''
#     while n!=0:
#         r=n%10
#         a=list[r] + a
#         n=n//10
#     return a

# a=open("ostad.txt","r")
# text=a.readlines()
# b=open("shagerd.txt","w")
# for i in range(len(text)):
#     b.write(ad(i+1)+'. '+text[i])
# b.close()
# a.close()
# -----------
# f=open("golabi.txt","r")
# mystr=f.read()
# list1=[]
# for i in mystr:
#     if i not in "aAiIoOeEuU":
#         list1.append(i)
# list1="".join(list1)
# f=open("glb.txt","w")
# f.write(list1)
# -----------
# f = open("sib.txt","r")
# y = f.readlines()
# f.close()
# y=" ".join(y)
# y=y.split(" ")
# print(y)
# o = input()
# u = input()
# for i in y:
#     if o == i:
#         r=y.index(i)
#         del y [r]
#         y.insert(r,u)
# y=" ".join(y)
# t=open("moz.txt","w")
# t.write(y)
# t.close()




n=int(input())
x=int(input())
a=[]
for i in range (n):
    a.append(int(input()))
for i in range (x):
    c=a.pop(len(a)-1)
    a.insert(0,c)
print(a)
