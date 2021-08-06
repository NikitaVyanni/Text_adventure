import pygame
import pygame.freetype
import random


def move_player():
    player.y += player_speed
    if player.top < 0:
        player.top = 0
    if player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT


def restart_ball(dx, dy):
    ball.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    dx = random.choice([random.randint(-9, -3), random.randint(3, 9)])
    dy = random.choice([random.randint(-9, -3), random.randint(3, 9)])
    return dx, dy


def crash_ball(dx, dy):
    if ball.bottom > SCREEN_HEIGHT or ball.top < 0:
        dy *= -1
    if ball.colliderect(player) or ball.colliderect(enemy):
        dx *= -1
    if game_over == False:
        ball.x += dx
        ball.y += dy
    return dx, dy


def move_enemy():
    if ball.bottom < enemy.top:
        enemy.y -= enemy_speed
    if ball.top > enemy.bottom:
        enemy.y += enemy_speed


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ping-pong')

BG_COLOR = (21, 126, 26)

player = pygame.Rect(0, 0, 25, 100)
enemy = pygame.Rect(SCREEN_WIDTH - 25, 0, 25, 100)
ball =  pygame.Rect(SCREEN_WIDTH/2-10, SCREEN_HEIGHT/2-10, 20, 20)

enemy_speed = 7
ball_speed_x = random.choice([random.randint(-9, -3), random.randint(3, 9)])
ball_speed_y = random.choice([random.randint(-9, -3), random.randint(3, 9)])
player_speed = 0
player_score = 0
enemy_score = 0
game_over = False

font = pygame.freetype.Font('Mandhor-ALEmp.otf', 32)
win_font = pygame.freetype.Font('Mandhor-ALEmp.otf', 64)

# pong_sound = pygame.mixer.Sound('')
# pong_sound.play()

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_speed -= 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_speed += 10
            if event.key == pygame.K_r or event.key == pygame.K_RIGHT and game_over:
                player_score, enemy_score = 0, 0
                game_over = False
        if event.type == pygame.KEYUP:
            player_speed = 0

                # if event.key == pygame.K_e:
                #     running = exit

    # exit = running * 0

    # Update
    move_player()
    move_enemy()
    ball_speed_x, ball_speed_y = crash_ball(ball_speed_x, ball_speed_y)

    if ball.left > SCREEN_WIDTH:
        player_score += 1
    if ball.right < 0:
        enemy_score += 1

    if ball.left > SCREEN_WIDTH or ball.right < 0:
        ball_speed_x, ball_speed_y = restart_ball(ball_speed_x, ball_speed_y)

    # Draw
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (0, 0, 0), player)
    pygame.draw.rect(screen, (0, 0, 0), enemy)
    pygame.draw.line(screen, (255, 255, 255), (SCREEN_WIDTH/2, 0),
                                    (SCREEN_WIDTH/2, SCREEN_HEIGHT), 2)
    font.render_to(screen, (SCREEN_WIDTH/4, 150), str(player_score))
    font.render_to(screen, (SCREEN_WIDTH/1.5, 150), str(enemy_score))

    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    if player_score == 2: # (╯°□°）╯︵ ┻━┻
        win_font.render_to(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 'win!',
                                                                (255, 255, 0))
        game_over = True
    elif enemy_score == 2:# (╯°□°）╯︵ ┻━┻
        win_font.render_to(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 'game over!',
                                                                (255, 255, 0))
        game_over = True

    clock.tick(60)
    pygame.display.flip()
