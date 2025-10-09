import pygame
import random
score = 0
speed = 15
speedblockx = random.randint(50, 950)
speedblocky = random.randint(50, 750)
pygame.init()
screen = pygame.display.set_mode((1000, 800))
bg = pygame.image.load("recycle marathon/image/bg.png")
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recycle marathon/image/bin.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

class Nonrecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recycle marathon/image/bag.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

images = ["recycle marathon/image/paper bag.png", "recycle marathon/image/box.png", "recycle marathon/image/pen.png"]

itemlist = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plasticlist = pygame.sprite.Group()
specialblocklist = pygame.sprite.Group()
#creating item sprites

for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randint(50, 950)
    item.rect.y = random.randint(50, 750)
    itemlist.add(item)
    allsprites.add(item)

for i in range(15):
    plastic = Nonrecyclable()
    plastic.rect.x = random.randint(50, 950)
    plastic.rect.y = random.randint(50, 750)
    allsprites.add(plastic)
    plasticlist.add(plastic)


speedblock = pygame.draw.rect(screen, (500, 400, 40, 40))
specialblocklist.add(speedblock)
allsprites.add(speedblock)

bin = Bin()
allsprites.add(bin)
bin.rect.x = random.randint(50, 950)
bin.rect.y = random.randint(50, 750)

run = True
while run:
    screen.blit(bg, (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            bin.rect.x -= speed
        elif keypressed[pygame.K_UP]:
            bin.rect.y -= speed
        elif keypressed[pygame.K_RIGHT]:
            bin.rect.x += speed
        elif keypressed[pygame.K_DOWN]:
            bin.rect.y += speed
        itemhitlist = pygame.sprite.spritecollide(bin, itemlist, True)
        speedblockhitlist = pygame.sprite.spritecollide(bin, specialblocklist, True)
        plastichitlist = pygame.sprite.spritecollide(bin, plasticlist, True)
        allsprites.draw(screen)
        for i in itemhitlist:
            score += 1
        for i in plastichitlist:
            score -= 1
        for i in speedblockhitlist:
            speed += 15
        font = pygame.font.SysFont("Ariel", 20)
        text = font.render("score = " + str(score), True, "black")
        screen.blit(text, (50, 50))
        pygame.display.update()