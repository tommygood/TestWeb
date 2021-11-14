import pygame as pg, random, math, time

class Ball(pg.sprite.Sprite):
    dx = 0         
    dy = 0         
    x = 0          
    y = 0          
    direction = 0  
    speed = 0      
    
    def __init__(self, sp, srx, sry, radium, color):
        pg.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        self.image = pg.Surface([radium*2, radium*2])  
        self.image.fill((255,255,255))
        pg.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  
        self.rect.center = (srx,sry)       
        self.direction = random.randint(40,70)  

    def update(self,judge):         
        radian = math.radians(self.direction)    
        self.dx = self.speed * math.cos(radian) 
        self.dy = -self.speed * math.sin(radian) 
        self.x += self.dx     
        self.y += self.dy
        self.rect.x = self.x 
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  
            self.bouncelr()
            self.rect.top = 10
            self.bounceup()
        if judge :
            self.rect = self.image.get_rect()
            self.rect.center = (300,350)
        if(self.rect.bottom >= screen.get_height()-10): 
            return True
        else:
            return False
 
    def bounceup(self):  
        self.direction = 360 - self.direction

    def bouncelr(self): 
        self.direction = (180 - self.direction) % 360
           
class Brick(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([38, 13]) 
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pad(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("pikachu.png")  
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  
        self.rect.y = screen.get_height() - self.rect.height - 30
        
    def update(self):  
        pos = pg.mouse.get_pos()  
        self.rect.x = pos[0]       
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

def gameover(message): 
    global running
    text = ffont.render(message, 1, (255,0,255))  
    screen.blit(text, (screen.get_width()/2-150,screen.get_height()/2-20))
    pg.display.update() 
    time.sleep(5)        
    running = False      

pg.init()
score = 0  
dfont = pg.font.SysFont("Arial", 20)   
ffont = pg.font.SysFont("SimHei", 32)   
#soundhit = pg.mixer.Sound("media\\hit.wav")  
#soundpad = pg.mixer.Sound("media\\pad.wav")  
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("Sean's Brick Game")
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pg.sprite.Group()  
bricks = pg.sprite.Group()     
ball = Ball(15, 300, 350, 10, (255,123,188)) 
allsprite.add(ball)  
pad = Pad()         
allsprite.add(pad)   
for row in range(0, 5):          
    for column in range(0, 15): 
        if row == 1 or row == 0: 
            brick = Brick((153,205,255), column * 40 + 1, row * 15 + 1)   
        if row == 2: 
            brick = Brick((94,175,254), column * 40 + 1, row * 15 + 1)    
        if row == 3 or row == 4:  
            brick = Brick((52,153,207), column * 40 + 1, row * 15 + 1)  
        bricks.add(brick)    
        allsprite.add(brick)  
        
clock = pg.time.Clock()        
downmsg = "Press Left Click Button to start game!"  
playing = False  
running = True

while running:
    clock.tick(40)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    buttons = pg.mouse.get_pressed()  
    if buttons[0]:                 
        playing = True
    
    if playing == True:  
        screen.blit(background, (0,0))  
        fail = ball.update(False) 
        if fail:
            score = 0
            fail = False
            ball.update(True)
            continue
            #gameover("You failed!See you next time~")
        pad.update()          
        hitbrick = pg.sprite.spritecollide(ball, bricks, True)  
        if len(hitbrick) > 0: 
            score += len(hitbrick)  
            #soundhit.play()   
            ball.rect.y += 20  
            ball.bounceup()    
            if len(bricks) == 0:  
                gameover("Congratulations!!")
        hitpad = pg.sprite.collide_rect(ball, pad)  
        if hitpad:  
            #soundpad.play()  
            ball.bounceup()  
        allsprite.draw(screen)  
        downmsg = "Score: " + str(score)
    message = dfont.render(downmsg, 1, (255,0,255))
    screen.blit(message, (screen.get_width()/2-125,screen.get_height()-30))
    pg.display.update()
pg.quit()