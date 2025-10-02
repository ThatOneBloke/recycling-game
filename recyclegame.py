import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recycle marathon/image/bin.png")
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()

class Nonrecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recycle marathon/image/bag.png")
        self.rect = self.image.get_rect()

images = ["recycle marathon/image/paper bag.png", "recycle marathon/image/box.png", "recycle marathon/image/pen.png"]

itemlist = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plasticlist = pygame.sprite.Group()
#creating item sprites

for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randint(50, 450)
    item.rect.y = random.randint(50, 450)
    itemlist.add(item)
    allsprites.add(item)

for i in range(15):
    plastic = Nonrecyclable()
    plastic.rect.x = random.randint(50, 450)
    platic.rect.y = random.randint(50, 450)
    allsprites.add(plastic)
    plasticlist.add(plastic)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")
    pygame.display.update()