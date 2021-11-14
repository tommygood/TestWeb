import pygame,random
pygame.init()  
GREEN = (0,255,0) 
RED = (255,0,0) 
BLUE = (0,0,255) 
WHITE = (255,255,255) 
BLACK = (0,0,0) 
YELLOW = (255,255,0) 

class Object1(pygame.sprite.Sprite) :
    def __init__(self,spe) :
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((1280,640)) # scale of canvas，(x of windows*2,y of windows*2) will fill
        #self.image.fill(YELLOW)
        #self.speed = spe
        self.image = pygame.image.load("pikachu.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        randomX = random.randint(100,500)
        randomY = random.randint(50,320)
        self.rect.center = ((randomX,randomY)) # location of object
    
    def update(self) : # movement of object
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        
def main():
    width, height = 640, 320
    screen = pygame.display.set_mode((width, height))  
    pygame.display.set_caption("foundation")  
    background = pygame.Surface((320,160))  
    background = background.convert() 
    background.fill((0,255,255)) 
    running = True
    allSprite = pygame.sprite.Group()
    object1 = Object1(2)
    allSprite.add(object1)
    clock = pygame.time.Clock()
    times = 0 
    while running:  
        clock.tick(1) # run how many times in a second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False
        screen.blit(background, (320,0))  
        pygame.display.update()      
        object1.update()
        allSprite.draw(screen)
        pygame.display.update()      
    pygame.quit()

if __name__ == "__main__" :
    main()
    