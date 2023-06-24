from pygame import*

width = 600
height = 600

mw = display.set_mode((width, height))
mw.fill((100, 100, 255))
display.set_caption("Пінг Понг")
clock = time.Clock()

FPS = 60
game = True
while game:
    for e in event.get():
            if e.type == QUIT:
                  game = false

    display.update()
    clock.tick(FPS)