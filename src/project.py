import pygame

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CatFightingGame")


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



def main():

    run = True
    while run:

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__": main()            