from pygame import*
import pygame


pygame.init()
#print dos modulos do display (ve funções)
print("modos do display")
print(dir(pygame.display))

#size da window
x=800
y=600
z=[x,y]

pygame.display.set_caption("Game window") #da nome a janela

# inicializa a janela
surface=pygame.display.set_mode(z)

#cores
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
rose=(255,0,255)
print(pygame.image.get_extended())

#upload e tratamento de imagens
picture =pygame.image.load('space_fundo.bmp') #so da para extensoes bmp n sei pk
background= pygame.transform.scale(picture , z)# mete a imagem esticada para cobrir o screen
picture2=pygame.image.load('alien-cartoon.bmp') 
alien=pygame.transform.scale(picture2 , (100,100))
picture3=pygame.image.load('spacecraft.bmp')
ship=pygame.transform.scale(picture3 , (300,300))





#mantem janela aberta (loop) ate quit
window= True
while window:
  for event in pygame.event.get():  #recebe os clickes etc
    if event.type==pygame.QUIT:
      window=False
  #coloca a janela com cor branca (tem de fazer update)
  surface.fill(white)#colocar a branco se deixar fia a fazer loops
  surface.blit(background,(0,0))#pygame.display.set_mode(z).blit(background,(z)), coloca o fundo na posicao 0,0
  surface.blit(alien,(350,100))
  surface.blit(ship,(250,350))
  pygame.display.update()
 
pygame.quit()
















# def my_function():
#   print("Hello from a function")

# my_function()
