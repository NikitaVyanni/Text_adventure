import pygame


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650

def move_player():
    player.y += player_speed_y
    player.x += player_speed_x
    if player.top < 0:
        player.top = 0
    if player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

player_speed_x = 0
player_speed_y = 0



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False)


BG_COLOR = (235, 217, 92)


player = pygame.Rect(0, 0, 50, 50)
aim = pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 10, 10)
running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed_y -= 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed_y += 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_speed_x -= 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_speed_x += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed_y += 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed_y -= 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_speed_x += 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_speed_x -= 10



    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (0, 0, 0), player)
    pygame.draw.ellipse(screen, (255, 0, 0), (pygame.mouse.get_pos(), (20, 20)), 1)
    # pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 5)
    pygame.display.set_caption(str(int(clock.get_fps())))


    move_player()


    clock.tick(60)
    pygame.display.flip()
