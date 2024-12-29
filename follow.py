import pygame
import os
import sys

FPS = 60
speed_x = 0
speed_y = 0

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
    return image


def moving(main_pos, pos):
    global speed_y, speed_x
    if (main_pos[0] - pos[0]) < 0:
        speed_x = -1
    elif (main_pos[0] - pos[0]) > 0:
        speed_x = 1
    if (main_pos[1] - pos[1]) > 0:
        speed_y = 1
    elif (main_pos[1] - pos[1]) < 0:
        speed_y = -1
    return pos[0] + (main_pos[0] - pos[0]) // 50 + speed_x, pos[1] + (main_pos[1] - pos[1]) // 50 + speed_y


def checking(main_pos, angry_pos):
    if main_pos[0] - 5 <= angry_pos[0] - 8 <= main_pos[0] + 5 and main_pos[1] - 5 <= angry_pos[1] <= main_pos[1] + 5:
        return False
    elif main_pos[0] - 5 <= angry_pos[0] + 8 <= main_pos[0] + 5 and main_pos[1] - 5 <= angry_pos[1] <= main_pos[1] + 5:
        return False
    elif main_pos[1] - 5 <= angry_pos[1] + 8 <= main_pos[1] + 5 and main_pos[0] - 5 <= angry_pos[0] <= main_pos[0] + 5:
        return False
    elif main_pos[1] - 5 <= angry_pos[1] - 8 <= main_pos[1] + 5 and main_pos[0] - 5 <= angry_pos[0] <= main_pos[0] + 5:
        return False
    return True


def draw_main(screen, main_pos, angry_pos, bg):
    screen.blit(bg, (0, 0))
    pygame.draw.circle(screen, 'red', main_pos, 10)
    pygame.draw.circle(screen, 'black', angry_pos, 15)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    background = load_image('background1.jpeg')
    background = pygame.transform.scale(background, (500, 500))
    screen.blit(background, (0, 0))
    running = True
    flag = True

    coords_main = (250, 250)
    coords_angry = (480, 20)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if 70 <= event.pos[0] <= 430 and 90 <= event.pos[1] <= 440:
                    coords_main = event.pos
        if flag:
            draw_main(screen, coords_main, coords_angry, background)
            if not checking(coords_main, coords_angry):
                flag = False
                screen.blit(background, (0, 0))
                pygame.draw.rect(screen, 'black', [30, 120, 440, 240])
                font = pygame.font.Font(None, 85)
                text = font.render('Ты проиграл!', True, (255, 255 , 255))
                screen.blit(text, (60, 200))
            clock.tick(FPS)
            coords_angry = moving(coords_main, coords_angry)
            pygame.display.flip()
    pygame.quit()
