import pygame
import time
# rezayi , arshi , mohammadi , sedighian , naimi , zomorodin
pygame.init()

pygame.display.set_caption("test")

img = pygame.image.load("32.png")
img_width , img_height = img.get_size()

screen = pygame.display.set_mode((img_width,img_height))

for i in range(img_width):
    for j in range(img_height):
        r,g,b,a = img.get_at((i,j))
        mean = (r + g + b) // 3
        img.set_at((i,j),(mean,mean,mean))
        


        
screen.blit(img,(0,0))
pygame.display.update()





time.sleep(10)