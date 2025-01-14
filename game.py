import pygame
import os

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Odbyt")
white = (255, 255, 255)
black = (0,0,0)
RED = (255,0,0)
yellow = (255, 255, 0)
BORDER = pygame.Rect(width//2 - 5, 0, 10, height)
FPS = 60
vel = 5
bullet_vel = 7
max_bullets = 3
spaceship_width, spaceship_height = 80,65
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2
yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image,(spaceship_width,spaceship_height)),90)
red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image,(spaceship_width,spaceship_height)),270)
space = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (width,height))

def draw_windows(red,yellow, red_bullets, yellow_bullets):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen, black, BORDER)
    screen.blit(yellow_spaceship,(yellow.x,yellow.y))
    screen.blit(red_spaceship,(red.x,red.y) )
    for bullet in red_bullets:
        pygame.draw.rect(screen, RED, bullet )

    for bullet in yellow_bullets:
        pygame.draw.rect(screen, (255,255,0), bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0: #LEFT
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < BORDER.x: #RIGHT
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0: #UP
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and  yellow.y + vel + yellow.height < height - 10 : #DOWN
        yellow.y += vel


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x + BORDER.width: #LEFT
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < width: #RIGHT
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y - vel > 0: #UP
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < height - 10 : #DOWN
        red.y += vel

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet )

def main():
    red = pygame.Rect(1100,300, spaceship_width,spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed,red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_windows(red,yellow, red_bullets, yellow_bullets)

    pygame.quit()




if __name__ == "__main__":
    main()
