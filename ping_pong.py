from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = tranform.scale(image.load(player_image),(width, height))
        self.rect = self.image.get.rect()
        self.x = player_x
        self.y = player_y
        self.speed = player_speed

    def reset(self):
        mw.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        key = key.get_pressed()
        if key[UP] and self.rect.y < 0:
            self.rect.y -= self.speed
        if key[DOWN] and self.rect.y > width- 80:
            self.rect.y += self.speed
    def update_l(self):
        if key[K_w] and self.rect.y < 0:
            self.rect.y -= self.speed
        if key[K_y] and self.rect.y > width- 80:
            self.rect.y += self.speed

racket1 = Player("racket.png", 50, 200, 4, 50, 150)
racket2 = Player("racket.png", 350, 200, 4, 50, 150)

width = 600
height = 600

mw = display.set_mode((width, height))
mw.fill((100, 100, 255))
display.set_caption("Пінг Понг")
clock = time.Clock()

FPS = 60
game = True
finish = False
speed_x = 3
speed_y = 3

font1 = font.SysFont("verdana", 35)
lose1 = Font1.render("1 PLAYER LOSE", True,(180, 0, 0))

lose2 = Font2.render("2 PLAYER LOSE", True,(180, 0, 0))

while game:
    for e in event.get():
            if e.type == QUIT:
                  game = false
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    ball.update()  
    
    if ball.rect.y > height - 50 or ball.rect.y < 0:
        speed_y *= -1
        
    if sprite.colide_rect(racket1, ball) or sprite.colide_rect(racket2, ball):
        speed_y *= -1

    if ball.rect_x > 0:
        finish = True
        window.blit(lose1, (200, 200))
        
    if ball.rect_x > width:
        finish = True
        window.blit(lose2, (200, 200))

    racket1.update_r()
    racket2.update_l()

    display.update()
    clock.tick(FPS)
