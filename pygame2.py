# import pygame
# import time

# pixel hastan width?! , None javab nemide... , tabe bazgashti ok e?! , 
# zekhamat ha be kodoom samt ezafe mishe



# pygame.init()

# screen = pygame.display.set_mode((400,400))

# screen.fill((100,100,100))

# pygame.draw.line(screen,(255,0,0),(400,100),(400,200),10)
# pygame.draw.circle(screen,'blue',(200,200),100,3)
# pygame.draw.rect(screen,'red',(0,0,400,400),1)
# pygame.draw.ellipse(screen,'red',(0,0,100,50),1)
# pygame.draw.polygon(screen,'red',((0,0),(100,100),(100,0),(0,100)),0)


# myfont = pygame.font.Font(None,100) 
# text = myfont.render("hello world!",True,(255,0,0))

# screen.blit(text,(0,0))


# pygame.mixer.music.load("/home/mahdi/Desktop/helli/04_05/codes/arsenal.mp3")
# pygame.mixer.music.play(-1,20)

# pygame.mixer.music.stop()


# img = pygame.image.load("/home/mahdi/Desktop/helli/04_05/codes/Declan-Rice-for-Arsenal-vs-Real-Madrid-in-the-UCL.jpg")
# w,h = img.get_size()
# screen = pygame.display.set_mode((w,h))
# screen.blit(img,(0,0))

# pygame.display.update()
# time.sleep(20)


# 1. behrad 1 , 
# import pygame
# import time
# import random
# pygame.init()
# screen = pygame.display.set_mode((1000, 1000))
# while 0==0:
#     a=random.randint(0 ,255)
#     b=random.randint(0 ,255)
#     c=random.randint(0 ,255)
#     screen.fill((a ,b ,c))
#     pygame.display.update()
#     time.sleep(5)

# --------------
# motevaseli + 
# import pygame
# import time

# pygame.init()

# screen = pygame.display.set_mode((500,500))

# screen.fill((255,0,0))

# pygame.draw.line(screen,(255,0,0),(100,100),(200,200),1)
# pygame.draw.circle(screen,(255,0,0),(100,100),100,0)
# pygame.draw.rect(screen,(255,0,0),(0,0,100,50),10)
# pygame.draw.ellipse(screen,(255,0,0),(100,100,100,50))
# pygame.draw.polygon(screen,(255,0,0),((100,100),(200,200),(400,300)),1)


# myfont = pygame.font.Font("/usr/share/fonts/type1/urw-base35/C059-BdIta.t1",24)
# text = myfont.render('Hello World!',True,(255,0,0))
# screen.blit(text,(0,0))

# pygame.mixer.music.load("arsenal.mp3")
# pygame.mixer.music.play(1,20)
# # pygame.mixer.music.stop()

# img = pygame.image.load("/home/mahdi/Desktop/helli/04_05/codes/Declan-Rice-for-Arsenal-vs-Real-Madrid-in-the-UCL.jpg")
# w,h = img.get_size()
# screen = pygame.display.set_mode((w,h))
# screen.blit(img,(0,0))

# pygame.display.update()

# time.sleep(10)


# 1. yazdan , sajad , mani , mehrbod, motevaseli
# import pygame
# import random
# import time

# pygame.init()


# screen = pygame.display.set_mode((500 , 500))

# while True :
#     r = random.randint(0 , 255)
#     g = random.randint(0 , 255)
#     b = random.randint(0 , 255)
#     screen.fill((r , g , b))
#     pygame.display.update()
#     time.sleep(5)

# hemmati , momeni , heidarzade , sedighian
# import pygame
# import random
# import time
# y = 1390
# m = 8
# d = 17
# ty = 1400
# tm = 6
# td = 12
# age = (ty-y)+(tm-m)/12+(td-d)/365
# age = int(age*100)/100
# pygame.init()
# screen = pygame.display.set_mode((600,400))
# font = pygame.font.Font(None,80)
# color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
# text = font.render(str(age),True,(255,255,255))
# screen.fill((255, 255, 255))
# pygame.draw.rect(screen,color,(200,160,200,80))
# screen.blit(text,(250,170))
# pygame.display.update()
# time.sleep(10)

# -----------------------------
# ali arsha , 

# import pygame
# import time

# pygame.init()

# screen = pygame.display.set_mode((500,500))

# screen.fill((200,200,200))


# pygame.draw.line(screen,'blue',(100,100),(200,200),1)
# pygame.draw.circle(screen,(255,0,0),(200,200),100,1)
# pygame.draw.rect(screen,(255,0,0),(0,0,50,100),0)
# pygame.draw.ellipse(screen,'blue',(0,0,100,50),0)
# pygame.draw.polygon(screen,(0,255,0),((100,100),(200,200)),1)



# myfont = pygame.font.Font("/usr/share/fonts/type1/urw-base35/C059-BdIta.t1",24)
# text = myfont.render("Hello World!",True,(255,0,0))
# screen.blit(text,(0,0))


# pygame.mixer.music.load("/home/mahdi/Desktop/helli/04_05/codes/arsenal.mp3")
# pygame.mixer.music.play(-1,0)

# pygame.mixer.music.stop()



# img = pygame.image.load("/home/mahdi/Desktop/helli/04_05/codes/Declan-Rice-for-Arsenal-vs-Real-Madrid-in-the-UCL.jpg")
# w,h = img.get_size()
# screen = pygame.display.set_mode((w,h))
# screen.blit(img,(0,0))

# pygame.display.update()

# time.sleep(10)

# ---------------------------
# font not intialized ... 
import pygame
import time

pygame.init()

# screen = pygame.display.set_mode((500,500))

# screen.fill((255,0,0))


# pygame.draw.line(screen,(255,0,0),(100,100),(200,200),1)
# pygame.draw.circle(screen,(255,0,0),(100,100),50,10)
# pygame.draw.rect(screen,(255,0,0),(0,0,50,100),0)
# pygame.draw.ellipse(screen,(255,0,0),(100,100,100,50),1)
# pygame.draw.polygon(screen,(255,0,0),((100,100),(200,200),(400,300)),1)


# font = pygame.font.Font("/usr/share/fonts/type1/urw-base35/C059-BdIta.t1",24)
# text = font.render('Hello World!',True,(255,0,0))
# screen.blit(text,(0,0))


# pygame.mixer.music.load("/home/mahdi/Desktop/helli/04_05/codes/arsenal.mp3")
# pygame.mixer.music.play(-1,20)

# pygame.mixer.music.stop()


# img = pygame.image.load("/home/mahdi/Desktop/helli/04_05/codes/Declan-Rice-for-Arsenal-vs-Real-Madrid-in-the-UCL.jpg")
# w,h = img.get_size()
# screen = pygame.display.set_mode((w,h))
# screen.blit(img,(0,0))


pygame.display.update()
time.sleep(10)
