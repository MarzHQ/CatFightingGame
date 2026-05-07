import pygame

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CatFightingGame")

clock = pygame.time.Clock()
FPS = 60
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

COWBOY_SIZE = 162
COWBOY_SCALE = 4
COWBOY_OFFSET = [72, 70]
COWBOY_DATA = [COWBOY_SIZE, COWBOY_SCALE, COWBOY_OFFSET]
ALIEN_SIZE = 162
ALIEN_SCALE = 4
ALIEN_OFFSET = [72, 70]
ALIEN_DATA = [ALIEN_SIZE, ALIEN_SCALE, ALIEN_OFFSET]

pygame.mixer.music.load("audio/pixelparadise.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0, 5000)

alienhit_fx = pygame.mixer.Sound("audio/alienhit.wav")
alienhit_fx.set_volume(0.5)
hit_fx = pygame.mixer.Sound("audio/hit.wav")
hit_fx.set_volume(0.5)

bg_image = pygame.image.load("images/Background/BackgroundGame.jpg").convert_alpha()

cowboy_sheet = pygame.image.load("images/cowboycat/cowboycat.png").convert_alpha()
alien_sheet = pygame.image.load("images/aliencat/aliencat.png").convert_alpha()

victory_img = pygame.image.load("images/icons/victoryRoyale.png").convert_alpha()

count_font = pygame.font.Font("fonts/SuperAdorable.ttf", 80)
score_font = pygame.font.Font("fonts/SuperAdorable.ttf", 30)

COWBOY_ANIMATION_STEPS = [1, 8, 1, 7, 7, 3 ,7]
ALIEN_ANIMATION_STEPS = [1, 8, 1, 7, 7, 3 ,7]

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0,0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

class Fighter():
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_sound = sound
        self.hit = False
        self.alive = True
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):

        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0
        key = pygame.key.get_pressed()

        if self.attacking == False and self.alive == True and round_over == False:
            if self.player == 1:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(target)
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(target)
                    if key[pygame.K_KP1]:
                        self.attack_type = 1
                    if key[pygame.K_KP2]:
                        self.attack_type = 2

def main():

    run = True
    while run:

        clock.tick(FPS)

        draw_bg()



        

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__": main()            