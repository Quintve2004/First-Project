import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Project @Quintve")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VEL = 7

def window_update(player_a, player_b):
    WIN.fill(WHITE)

    pygame.draw.rect(WIN, BLACK, player_a)
    pygame.draw.rect(WIN, BLACK, player_b)

    pygame.display.update()

def player_a_movement(keys_pressed, player_a):
    if keys_pressed[pygame.K_a] and player_a.x > 0:
        player_a.x -= VEL

    if keys_pressed[pygame.K_d] and player_a.x < (WIDTH - 100):
        player_a.x += VEL

    pygame.display.update()

def player_b_movement(keys_pressed, player_b):
    if keys_pressed[pygame.K_LEFT] and player_b.x > 0:
        player_b.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player_b.x < (WIDTH - 100):
        player_b.x += VEL

    pygame.display.update()

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    player_a = pygame.Rect(WIDTH/2 -5 , 50, 100, 10)
    player_b = pygame.Rect(WIDTH/2 -5 , HEIGHT-50, 100, 10)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        player_a_movement(keys_pressed, player_a)
        player_b_movement(keys_pressed, player_b)

        window_update(player_a, player_b) #Updates UI

# Initialize pygame
if __name__ == "__main__":
    main()