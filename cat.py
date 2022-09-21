import pygame
import random

pygame.init()
dis = pygame.display.set_mode((1020, 600))
pygame.display.set_caption('Cat')
clock = pygame.time.Clock()
time = 13


pink = (255,105,80)
white = (255,255,255)
black = (0,0,0)
img_fon = pygame.image.load('фон.jpg')
img_fon2 = pygame.image.load('фон 2.png')
player = [pygame.image.load('котобрез.png'), pygame.image.load('кот обркз2.png'), pygame.image.load ('котобрез3.png')]
food_img = pygame.image.load('рыбеха.png')
food_img2 = pygame.image.load('стейк.png')

# pygame.mixer.music.load('Балтийская улица (1).wav')
# pygame.mixer.music.play()
song = pygame.mixer.Sound('Балтийская улица (1).wav')


x = 20
y = 400
food_random = random.choice([food_img2, food_img])
x1 = random.randrange(450, 1000, 20)
y1 = random.choice([280, 180])
x_change = 0
y_change = 0
jump = 9
jump2 = 10
isjump = False
isjump2 = False
animation_count = 0
font_count = 0
fon_img_x = 0
fon_img2_x = 1020


def animation():

    global animation_count
    dis.blit(player[animation_count], (x, y))
    pygame.display.update()
    if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
        animation_count += 1
        if animation_count == 3:
            animation_count = 0
    if isjump == True:
        animation_count = 0


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and x <= 180:
        x += 10
        y += 0
    if key[pygame.K_RIGHT]:
        fon_img_x -= 10
        fon_img2_x -= 10
        x1 -= 10
        y1 += 0
    if key[pygame.K_LEFT]:
        x -= 10
        y += 0

    if not isjump:
        if key[pygame.K_SPACE]:
            isjump = True
    else:
        if jump != -10:
            y -= jump*4
            jump -= 1
        else:
            isjump = False
            jump = 9
    if not isjump2:
        if key[pygame.K_SPACE] and key[pygame.K_UP]:
            isjump2 = True
    else:
        if jump2 != -11:
            y -= jump2 * 4//2
            jump2 -= 1
        else:
            isjump2 = False
            jump2 = 10

    for q in range(x1-90, x1+90, 10):
        if x == q and y == y1:
            food_random = random.choice([food_img2, food_img])
            x1 = random.randrange(450, 900, 50)
            y1 = random.choice([280, 180])
            font_count += 1
            song.play()
        if x1 <= -100:
            food_random = random.choice([food_img2, food_img])
            x1 = random.randrange(450, 900, 50)
            y1 = random.choice([280, 180])




    # dis.fill(white)
    if fon_img2_x == 0:
        fon_img_x = 1020
    if fon_img_x == 0:
        fon_img2_x = 1020
    dis.blit(img_fon2, (fon_img2_x, 0))
    dis.blit(img_fon, (fon_img_x, 0))


    x += x_change
    y += y_change

    clock.tick(time)
    food = dis.blit(food_random, (x1, y1))
    font = pygame.font.SysFont('Helvetica',75)
    text = font.render(f'Очки: {font_count}', 5, black)
    dis.blit(text, (0, 0))


    animation()
    pygame.display.update()

pygame = quit()
quit()

