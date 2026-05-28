# mahmoodi
# import pygame
# import time
# pygame.init()


# s = pygame.display.set_mode((800, 800))

# r = 25
# x = 200
# y = 200
# dx = 3
# dy = 3

# while True:

#     x += dx
#     y += dy

#     if x - r <= 0:
#         x = r
#         dx = -dx
#     if x + r >= 800:
#         x = 800 - r
#         dx = -dx
#     if y - r <= 0:
#         y = r
#         dy = -dy
#     if y + r >= 800:
#         y = 800 - r
#         dy = -dy

#     if x + r >= 400 and x - r <= 405:
#         if y + r >= 350 and y - r <= 450:
#             if dx > 0 and x < 400:
#                 x = 400 - r
#                 dx = -dx
#             elif dx < 0 and x > 405:
#                 x = 405 + r
#                 dx = -dx
#             else:
#                 dy = -dy

#     s.fill((0, 0, 0))
#     pygame.draw.circle(s, (0, 0, 255), (x, y), r)
#     pygame.draw.rect(s, (0, 0, 255), (400, 350, 5, 100))
#     pygame.display.update()
#     time.sleep(0.001)

# ----------------------
# sina
# import pygame
# import time
# import random

# pygame.init()

# w = 800
# h = 800
# screen = pygame.display.set_mode((w, h))

# x = 100
# y = 400
# r = 25

# dx = 3
# dy = -3

# rect_x = 600
# rect_y = 350
# rect_w = 5
# rect_h = 100

# while True:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             raise SystemExit

#     oldx = x
#     oldy = y

#     x += dx
#     y += dy

   
#     if x + r >= w:
#         dx = -random.randint(1, 5)

#         if dy > 0:
#             dy = random.randint(1, 5)
#         else:
#             dy = -random.randint(1, 5)

#         x = w - r

    
#     if x - r <= 0:
#         dx = random.randint(1, 5)

#         if dy > 0:
#             dy = random.randint(1, 5)
#         else:
#             dy = -random.randint(1, 5)

#         x = r

   
#     if y + r >= h:
#         dy = -random.randint(1, 5)

#         if dx > 0:
#             dx = random.randint(1, 5)
#         else:
#             dx = -random.randint(1, 5)

#         y = h - r

    
#     if y - r <= 0:
#         dy = random.randint(1, 5)

#         if dx > 0:
#             dx = random.randint(1, 5)
#         else:
#             dx = -random.randint(1, 5)

#         y = r

    
#     if (x + r > rect_x and
#         x - r < rect_x + rect_w and
#         y + r > rect_y and
#         y - r < rect_y + rect_h):

#         if oldx + r <= rect_x:
#             dx = -random.randint(1, 5)

#             if dy > 0:
#                 dy = random.randint(1, 5)
#             else:
#                 dy = -random.randint(1, 5)

#         if oldx - r >= rect_x + rect_w:
#             dx = random.randint(1, 5)

#             if dy > 0:
#                 dy = random.randint(1, 5)
#             else:
#                 dy = -random.randint(1, 5)

#         if oldy + r <= rect_y:
#             dy = -random.randint(1, 5)

#             if dx > 0:
#                 dx = random.randint(1, 5)
#             else:
#                 dx = -random.randint(1, 5)

#         if oldy - r >= rect_y + rect_h:
#             dy = random.randint(1, 5)

#             if dx > 0:
#                 dx = random.randint(1, 5)
#             else:
#                 dx = -random.randint(1, 5)

#     screen.fill((255,255,255))
#     pygame.draw.rect(screen, (0,0,0), (rect_x, rect_y, rect_w, rect_h))
#     pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), r)

#     pygame.display.update()
#     time.sleep(0.01)

# -------------------

# import pygame
# import time
# import sys
# pygame.init()
# w = 800
# h = 800
# r = 25
# x = r
# y = h - r
# dx = 8
# dy = 5
# a = 200
# b = 350
# screen = pygame.display.set_mode((w , h))
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 if a - 2 > 0:
#                     a -= 2
#                 else:
#                     a = 0
#             if event.key == pygame.K_d:
#                 if (a + 5) + 2 < w:
#                     a += 2
#                 else:
#                     a = w - 7
#             if event.key == pygame.K_w:
#                 if b - 2 > 0:
#                     b -= 2
#                 else:
#                     b = 0
#             if event.key == pygame.K_s:
#                 if (b + 100) + 2 < h:
#                     b += 2
#                 else:
#                     b = h - 102
#             if event.key == pygame.K_SPACE:
#                 pygame.quit()
#                 sys.exit()
#     pygame.draw.circle(screen, (225, 225, 225), (x, y), r, 0)
#     pygame.draw.rect(screen, (225, 225, 225), (a, b, 5, 100), 0)
#     if (y + dy > h - r) or (y + dy < r) or (a <= x <= a + 5 and (b <= y + dy + r <= b + 100 or b <= y + dy - r <= b + 100)):
#         dy = -dy
#     if (x + dx > w - r) or (x + dx < r) or (b <= y <= b + 100 and (a <= x + dx + r <= a + 5 or a <= x + dx - r <= a + 5)):
#         dx = -dx
#     x += dx
#     y += dy
#     pygame.display.update()
#     screen.fill((0, 0, 0))
#     time.sleep(0.05)

# ------------------

# import pygame 
# import time
# pygame.init() 
# screen = pygame.display.set_mode((800,800))
# x=50
# y=700
# dx=2
# dy=-2
# pygame.draw.circle(screen,"red",(x,y),25,0)
# pygame.draw.rect(screen,"blue",(400,350,5,100),0)
# pygame.display.update()
# while True:
#     if x+dx+25>800:
#         dx=-1*dx
#     if (405>=x+dx+25>=400 or 405>=x+dx-25>=400) and (450>=y+25>=350 or 450>=y-25>=350):
#         dx=-1*dx
#     if x+dx-25<0:
#         dx=-1*dx
#     if y+dy+25>800:
#         dy=-1*dy
#     if (450>=y+dy+25>=350 or 450>=y+dy-25>=350) and (405>=x-25>=400 or 405>=x+25>=400):
#         dy=dy*-1
#     if y+dy-25<0:
#         dy=-1*dy
#     x=x+dx
#     y=y+dy
#     screen.fill((0,0,0))
#     pygame.draw.circle(screen,"red",(x,y),25,0)
#     pygame.draw.rect(screen,"blue",(400,350,5,100),0)
#     pygame.display.update()
#     time.sleep(0.01)


# ------------------
#sajad

# import pygame
# import time
# import random

# pygame.init()
# screen = pygame.display.set_mode((800,800))
# r = 25
# x = r
# y = 300

# dx = 1 # alamat dx ghabli 
# dy = -1
# sx = 1 # andaze dx ghabli 
# sy = 1
# mx = dx*sx # = dx
# my = dy*sy

# rect_w = 5
# rect_x = 100
# rect_y = 200
# rect_h = 100


# while 1==1:
#     nx = x+ mx
#     ny =y+ my
#     if ny+r>800 or ny-r<=0 :
#         dy = -dy
#         sy = random.randint(1,5)
#         sx =random.randint(1,5)
#     if nx+r>800 or nx-r<=0 :
#         dx = -dx
#         sy = random.randint(1,5)
#         sx =random.randint(1,5)

#     if nx + r > rect_x and nx - r < rect_x + rect_w and ny + r > rect_y and ny - r < rect_y + rect_h:
        
#         if nx + r <= rect_x + mx or nx - r >= rect_x + rect_w + mx:
#             dx = -dx
#         if ny + r <= rect_y + my or ny - r >= rect_y + rect_h + my:
#             dy = -dy
        
#         sy = random.randint(1,5)
#         sx = random.randint(1,5)


#     mx = dx * sx
#     my = dy * sy
#     screen.fill((0,0,0))
#     pygame.draw.circle(screen,(0,0,255),(x,y),r,0)
#     pygame.draw.rect(screen,'red',(rect_x,rect_y,rect_w,rect_h),0)
#     x=x+mx
#     y = y+my
#     pygame.display.update()
#     time.sleep(0.005)
    
