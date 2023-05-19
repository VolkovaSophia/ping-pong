from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.speed_y = speed
        self.speed_x = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Player(GameSprite):
        def __init__(self,image_name, x, y, speed, width, height, side):
            super().__init__(image_name, x, y, speed, width, height)
            self.side = side
        def update(self):
            keys = key.get_pressed()
            k1 = K_UP
            k2 = K_DOWN

            if self.side == 'l':
                k1 = K_w
                k2 = K_s

            if keys[k1] and self.rect.y >= 5:
                self.rect.y -= self.speed_y
            if keys[k2] and self.rect.y <= win_height - 150:
                self.rect.y += self.speed_y

bg = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(bg)

ball = GameSprite('tenis_ball.png', 200, 100, 2, 50, 50)
racket1 = Player('racket.png', 30, 200, 4, 50, 150, 'l')
racket2 = Player('racket.png', 520, 200, 4, 50, 150, 'r')

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(bg)
        ball.update()
        ball.reset()
        racket1.update()
        racket2.update()
        racket1.reset()
        racket2.reset()

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball.speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            ball.speed_y *= -1

        if ball.rect.left < 30:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.right > 550:
            finish = True
            window.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)