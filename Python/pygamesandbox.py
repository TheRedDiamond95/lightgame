import pygame

"Window Settings"
screen=pygame.display.set_mode((1280, 720))
pygame.display.set_caption('lightgame')

"Cosmetics"
backgroundcolor=(0, 0, 0)
screen.fill(backgroundcolor)

"Light Switches"
#Image Path
img=pygame.image.load('images/button.png').convert_alpha()

#Render Images
class Button:
  def __init__(self,x,y,image):
    self.image=image
    self.rect=self.image.get_rect()
    self.rect.topleft=(x,y)
  def draw(self):
    screen.blit(self.image(self.rect.x,self.rect.y))

#Create Instances
button= Button(100, 200, img)

"Running Game"
running=True
while running:
  pygame.display.flip()
  