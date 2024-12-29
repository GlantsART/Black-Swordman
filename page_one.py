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

def draw_text(screen):
    font = pygame.font.Font('C:/Users/MSI/AppData/Local/Microsoft/Windows/Fonts/kashimarusbycop.otf', 40)
    text1 = font.render('недавно с небес спустились ангелы...', True, (150, 11, 2))
    str1 = font.render('page 1', True, (150, 11, 2))
    text2 = font.render('К удивлению людей вместо помощи', True, (150, 11, 2))
    text3 = font.render('в бедствиях ангелы начали уничтожать', True, (150, 11, 2))
    text4 = font.render('землю. Это были падшие ангелы.', True, (150, 11, 2))
    text5 = font.render('Убив всех богов, они принялись уничтожать', True, (150, 11, 2))
    text6 = font.render('мир, а люди спрятались по землей.', True, (150, 11, 2))
    text61 = font.render('В мире воцарился заос и разруха.', True, (150, 11, 2))
    text7 = font.render('Кенси, потерял всю свою семью из за', True, (150, 11, 2))
    text8 = font.render('ангелов. Последний из богов перед смертью', True, (150, 11, 2))
    text9 = font.render('даровал Кенси силу - убивать ангелов', True, (150, 11, 2))
    text10 = font.render('и другую нечесть, которую не мог убить', True, (150, 11, 2))
    text11 = font.render('обычный человек.', True, (150, 11, 2))
    text12 = font.render('Охваченный ненависть, Кенси поклялся', True, (150, 11, 2))
    text13 = font.render('уничтожить всех падших ангелов', True, (150, 11, 2))
    text14 = font.render('и освободить человечество от гнета', True, (150, 11, 2))
    text15 = font.render('существ не подвласных им...', True, (150, 11, 2))
    font = pygame.font.Font(None, 150)
    paint1 = font.render('†', True, (150, 11, 2))

    screen.blit(text1, (1080, 20))
    screen.blit(text2, (1050, 60))
    screen.blit(text3, (1050, 100))
    screen.blit(text4, (1050, 140))
    screen.blit(text5, (1050, 180))
    screen.blit(text6, (1050, 220))
    screen.blit(text61, (1050, 260))
    screen.blit(text7, (1080, 340))
    screen.blit(text8, (1050, 380))
    screen.blit(text9, (1050, 420))
    screen.blit(text10, (1050, 460))
    screen.blit(text11, (1050, 500))
    screen.blit(text12, (1080, 580))
    screen.blit(text13, (1050, 620))
    screen.blit(text14, (1050, 660))
    screen.blit(text15, (1050, 700))
    screen.blit(paint1, (1400, 800))
    screen.blit(str1, (1388, 940))

    pygame.draw.rect(screen, ((150, 11, 2)), (1035, 10, 755, 980), width=2)


def main():
    pygame.init()
    size = 1800, 1000
    screen = pygame.display.set_mode(size)
    bg = load_image('photo1.jpeg')
    screen.blit(bg, (0, 0))
    draw_text(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    print(pygame.font.match_font('kashimarusbycop'))
    pygame.quit()


if __name__ == '__main__':
    main()
