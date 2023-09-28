import pygame
import os

width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("slow_life")
WHITE = (255,255,255)
slow_life_width, slow_life_height = 125,110
slow_life_image = pygame.image.load(os.path.join("SiemaSlowLife","slowlife.png"))
slow_life = pygame.transform.scale(slow_life_image,(slow_life_width,slow_life_height))
mapa = pygame.transform.scale(pygame.image.load(os.path.join("SiemaSlowLife","mapa.jpg")),(width,height))
vel = 5
FPS = 60


def draw_windows(slow):
    screen.blit(mapa,(0,0))
    screen.blit(slow_life,(slow.x,slow.y))
    pygame.display.update()


def dino_movement(keys_pressed,slow):
    def bordery():
        if slow.x <= 430:
            slow.x = 430


    if keys_pressed[pygame.K_a] and slow.x > 0:
        slow.x -= vel
        bordery()
    if keys_pressed[pygame.K_d] and slow.x + vel + slow.width < 1280:
        slow.x += vel
    if keys_pressed[pygame.K_w] and slow.y - vel > 0:
        slow.y -= vel
        bordery()
    if keys_pressed[pygame.K_s] and slow.y - vel + slow.height   < 720:
        slow.y +=  vel
        bordery()



def main():
    clock = pygame.time.Clock()
    slow = pygame.Rect(665,350,slow_life_width,slow_life_height)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        dino_movement(keys_pressed,slow)
        draw_windows(slow)
        #print(pygame.mouse.get_pos())
    pygame.quit()

if __name__ == "__main__":
    main()
