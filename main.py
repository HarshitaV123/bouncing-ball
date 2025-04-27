import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tennis Ball Game")

WHITE = (255, 255, 255)

racket_img = pygame.image.load("tennis_racquet.png")
racket_img = pygame.transform.scale(racket_img, (80, 10))
racket_width, racket_height = racket_img.get_size()
racket_x = (WIDTH - racket_width) // 2
racket_y = HEIGHT - 30
racket_speed = 7

tennis_ball_img = pygame.image.load("tennis_ball.png")
tennis_ball_img = pygame.transform.scale(tennis_ball_img, (20, 20))
ball_radius = tennis_ball_img.get_width() // 2
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = HEIGHT // 2
ball_dx = 4 * random.choice([-1, 1])
ball_dy = -4

score = 0
lives = 3
font = pygame.font.Font(None, 36)

running = True
game_over = False

while running:
    pygame.time.delay(15)
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and racket_x > 0:
            racket_x -= racket_speed
        if keys[pygame.K_RIGHT] and racket_x < WIDTH - racket_width:
            racket_x += racket_speed
        
        ball_x += ball_dx
        ball_y += ball_dy
        
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_dx = -ball_dx
        if ball_y - ball_radius <= 0:
            ball_dy = -ball_dy
        
        if (racket_y <= ball_y + ball_radius <= racket_y + racket_height and
                racket_x <= ball_x <= racket_x + racket_width):
            ball_dy = -ball_dy
            score += 1
        
        if ball_y + ball_radius >= HEIGHT:
            lives -= 1
            ball_x = random.randint(ball_radius, WIDTH - ball_radius)
            ball_y = HEIGHT // 2
            ball_dx = 4 * random.choice([-1, 1])
            ball_dy = -4
        
        # Check for win or lose
        if score >= 20:
            game_over = True
            win_text = font.render("You Win!", True, (0, 128, 0))
        elif lives <= 0:
            game_over = True
            win_text = font.render("Game Over!", True, (255, 0, 0))
        
        screen.blit(racket_img, (racket_x, racket_y))
        screen.blit(tennis_ball_img, (ball_x - ball_radius, ball_y - ball_radius))
        
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 100, 10))
    else:
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
    
    pygame.display.update()

pygame.quit()
