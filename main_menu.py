import pygame
import os
import sys

FPS = 100


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'backgrounds', name)
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

def draw_name(screen):
    font = pygame.font.Font('C:/Users/MSI/AppData/Local/Microsoft/Windows/Fonts/go3v2.ttf', 100)
    text = font.render('Black Swordman', True, (255, 255, 255)) # (255 ,255 ,255)
    screen.blit(text, (45, 25))
    font = pygame.font.Font('C:/Users/MSI/AppData/Local/Microsoft/Windows/Fonts/go3v2.ttf', 100)
    text = font.render('Black Swordman', True, (253, 255, 110)) # 253, 255, 110
    screen.blit(text, (55, 35))
    font = pygame.font.Font('C:/Users/MSI/AppData/Local/Microsoft/Windows/Fonts/go3v2.ttf', 100)
    text = font.render('Black Swordman', True, (0, 8, 54)) # 0, 8, 54 (110, 10, 4)
    screen.blit(text, (50, 30))

def draw_load(screen, load_x):
    pygame.draw.rect(screen, (0, 8, 54), pygame.Rect(45, 170, 710, 60))
    pygame.draw.rect(screen, (253, 255, 110), pygame.Rect(50, 175, load_x, 50))
    font = pygame.font.Font(None, 50)
    text = font.render('load...', True, (0, 8, 54))
    screen.blit(text, (75, 185))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 730
    screen = pygame.display.set_mode(size)
    background = load_image('background.jpeg')
    screen.blit(background, (0, 0))
    draw_name(screen)
    running = True
    ticks_load = [0, 0]
    load_x = 0
    pygame.display.flip()
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        ticks_load[0] += 1
        if ticks_load[0] == 10 and ticks_load[1] < 70:
            load_x += 10
            ticks_load[0] = 0
            ticks_load[1] += 1
            draw_load(screen, load_x)
        clock.tick(FPS)
    pygame.quit()
