import pygame
import os
import sys

FPS = 100


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


class Board:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 20
        self.top = 20
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, 'dark red', pygame.Rect(
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size),
                                 width=1)

    def get_click(self, pos):
        cell = self.get_cell(pos)

    def get_cell(self, mouse_pos):
        delta_x = (mouse_pos[0] - self.left) // self.cell_size + 1
        delta_y = (mouse_pos[1] - self.top) // self.cell_size + 1
        if delta_x < 1 or delta_x > self.width or delta_y < 1 or delta_y > self.height:
            return None
        else:
            return delta_x, delta_y


class Main_charactare(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.anim_now = '1'
        self.attack_now = '0'
        self.hurt_now = '0'
        self.attack_animation_flag = False
        self.hurt_animation_flag = False
        self.image = pygame.transform.scale(load_image(f'samurai/randered/baze.png'),
                                            (77, 88))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.dir = True
        self.rect.y = 100
        self.main_size = (100, 113)

    def update(self, *key):
        direct = key[0]
        state = key[1]
        if direct == '1' and not self.attack_animation_flag and not self.hurt_animation_flag:
            self.rect.y -= 7
        if direct == '2' and not self.attack_animation_flag and not self.hurt_animation_flag:
            if self.dir:
                self.image = pygame.transform.flip(self.image, True, False)
                self.dir = False
            self.rect.x -= 7
        if direct == '3' and not self.attack_animation_flag and not self.hurt_animation_flag:
            self.rect.y += 7
        if direct == '4' and not self.attack_animation_flag and not self.hurt_animation_flag:
            if not self.dir:
                self.dir = True
                self.image = pygame.transform.scale(load_image(f'samurai/randered/Run{self.anim_now}.png'),
                                                    self.main_size)
            self.rect.x += 7
        if direct == '5' and state == 'go' and not self.attack_animation_flag and not self.hurt_animation_flag:
            self.anim_now = str((int(self.anim_now)) % 8 + 1)
            print(self.anim_now)
            self.image = pygame.transform.flip(
                pygame.transform.scale(load_image(f'samurai/randered/Run{self.anim_now}.png'),
                                       self.main_size), not self.dir, False)
        if state == 'stay' and not self.attack_animation_flag and not self.hurt_animation_flag:
            self.image = pygame.transform.flip(
                pygame.transform.scale(load_image(f'samurai/randered/baze.png'),
                                       self.main_size), not self.dir, False)
        if direct == '6' and not self.hurt_animation_flag:
            self.attack_animation_flag = True
            self.attack_now = str((int(self.attack_now) + 1))
            print(self.attack_now)
            if self.attack_now <= '5':
                self.image = pygame.transform.flip(
                    pygame.transform.scale(load_image(f'samurai/randered/Attack{self.attack_now}.png'),
                                           self.main_size), not self.dir, False)
            elif self.attack_now == '9':
                self.image = pygame.transform.flip(
                    pygame.transform.scale(load_image(f'samurai/randered/baze.png'),
                                           self.main_size), not self.dir, False)
                self.attack_now = '0'
                self.attack_animation_flag = False
        if direct == '7' and not self.attack_animation_flag:
            self.hurt_animation_flag = True
            self.hurt_now = str((int(self.hurt_now) + 1))
            if self.hurt_now == '3':
                self.hurt_now = '2'
            self.image = pygame.transform.flip(
                pygame.transform.scale(load_image(f'samurai/randered/Protection{self.hurt_now}.png'),
                                       self.main_size), not self.dir, False)
            if state == 'stop':
                self.hurt_animation_flag = False
                self.hurt_now = '0'
                self.image = pygame.transform.flip(
                    pygame.transform.scale(load_image(f'samurai/randered/baze.png'),
                                           self.main_size), not self.dir, False)

    def get_pos(self):
        return self.rect.x + 120, self.rect.y + 10


def key_events(all_sprites, state):
    keys = list(pygame.key.get_pressed())
    flg = False
    if keys[4]:
        all_sprites.update('2', 'go')
        flg = True
    if keys[7]:
        all_sprites.update('4', 'go')
        flg = True
    if keys[22]:
        all_sprites.update('3', 'go')
        flg = True
    if keys[26]:
        all_sprites.update('1', 'go')
        flg = True
    if flg:
        return 'go'
    else:
        return 'stay'


def main_character_animation(screen, ticks_run, all_sprites, attack_flag, attack_ticks, protect_flag, protect_ticks, main_character, main_hp):
    state = 'stay'
    state = key_events(all_sprites, state)
    ticks_run += 1
    if ticks_run == 5:
        all_sprites.update('5', state)
        ticks_run = 0
    if attack_flag:
        attack_ticks += 1
        if attack_ticks <= 36:
            if attack_ticks % 4 == 0:
                all_sprites.update('6', '')
        else:
            attack_ticks = 0
            attack_flag = False
    if protect_flag:
        protect_ticks += 1
        if protect_ticks % 5 == 0:
            all_sprites.update('7', '')
    elif not protect_flag and protect_ticks > 0:
        all_sprites.update('7', 'stop')
        protect_ticks = 0
    return ticks_run, attack_flag, attack_ticks, protect_flag, protect_ticks


def main():
    pygame.init()
    size = 1800, 1000
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    main_charactare = Main_charactare()
    all_sprites.add(main_charactare)
    clock = pygame.time.Clock()
    main_hp = 150
    ticks_run = 0
    attack_flag = False
    attack_ticks = 0
    protect_flag = False
    protect_ticks = 0
    board = Board(29, 16, 60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                attack_flag = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                protect_flag = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                protect_flag = False
        screen.fill('black')
        # board.render(screen)
        ticks_run, attack_flag, attack_ticks, protect_flag, protect_ticks = main_character_animation(screen, ticks_run, all_sprites,
                                                                                               attack_flag,
                                                                                               attack_ticks, protect_flag, protect_ticks, main_charactare, main_hp)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
