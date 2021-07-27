import pygame

pygame.font.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Project @Quintve")

player_score_font = pygame.font.SysFont("Courier", 24)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VEL = 8
BALLVEL = 5

SCOREA = 0
SCOREB = 0

player_a_collide = pygame.USEREVENT + 1
player_b_collide = pygame.USEREVENT + 2

def window_update(player_a, player_b, ball, scoreA, scoreB):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, player_a)
    pygame.draw.rect(WIN, BLACK, player_b)
    pygame.draw.rect(WIN, BLACK, ball)

    score_text = player_score_font.render("Player a: {} Player b: {}".format(scoreA, scoreB), 1, BLACK )
    WIN.blit(score_text, (WIDTH/2 - score_text.get_width()/2, HEIGHT - (HEIGHT -10)))
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

def ball_movement(ball):
    ball.y -= BALLVEL
    if ball.y > HEIGHT:
        print("border")
        ball.x = HEIGHT/2 - 5
        ball.y = WIDTH/2 - 5

def collide_object(player_a, player_b, ball):
    if ball.colliderect(player_a):
        pygame.event.post(pygame.event.Event(player_a_collide))
    if ball.colliderect(player_b):
        pygame.event.post(pygame.event.Event(player_b_collide))


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    player_a = pygame.Rect(WIDTH/2 -5 , 50, 100, 10) #First player
    player_b = pygame.Rect(WIDTH/2 -5 , HEIGHT-50, 100, 10) #Second player

    ball = pygame.Rect(WIDTH/2 -5, HEIGHT/2 -5, 10, 10) #Ball
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        keys_pressed = pygame.key.get_pressed()
        player_a_movement(keys_pressed, player_a)
        player_b_movement(keys_pressed, player_b)

        ball_movement(ball)

        collide_object(player_a, player_b, ball)
        window_update(player_a, player_b, ball, SCOREA, SCOREA) #Updates UI

# Initialize pygame
if __name__ == "__main__":
    main()