import pygame
import os
from animacja import Player

pygame.init()
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
slowcik = Player()


def draw_windows():
    screen.blit(mapa,(0,0))
    # screen.blit(slow_life,(slow.x,slow.y))
    slowcik.update()
    slowcik.draw(screen)
    pygame.display.update()

def bordery():
    if slowcik.rect.x <= 430:
        slowcik.rect.x = 430
    if slowcik.rect.x >= width - slow_life_width:
        slowcik.rect.x = width - slow_life_width
    if slowcik.rect.y <= 0:
        slowcik.rect.y = 0
    if slowcik.rect.y >= height - slow_life_height:
        slowcik.rect.y = height - slow_life_height

def main():
    clock = pygame.time.Clock()
    # slow = pygame.Rect(665,350,slow_life_width,slow_life_height)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and event.key == pygame.K_a:
                    slowcik.DOWN_KEY, slowcik.LEFT_KEY, slowcik.FACING_LEFT = True, True, True
                if event.key == pygame.K_s and event.key == pygame.K_d:
                    slowcik.DOWN_KEY, slowcik.RIGHT_KEY, slowcik.FACING_LEFT = True, True, False
                if event.key == pygame.K_w and event.key == pygame.K_a:
                    slowcik.UP_KEY, slowcik.LEFT_KEY, slowcik.FACING_LEFT = True, True, True
                if event.key == pygame.K_w and event.key == pygame.K_d:
                    slowcik.UP_KEY, slowcik.RIGHT_KEY, slowcik.FACING_LEFT = True, True, False
                elif event.key == pygame.K_d:
                    slowcik.RIGHT_KEY, slowcik.FACING_LEFT = True, False
                elif event.key == pygame.K_a:
                    slowcik.LEFT_KEY, slowcik.FACING_LEFT = True, True
                elif event.key == pygame.K_w:
                    slowcik.UP_KEY, slowcik.FACING_LEFT = True, False
                elif event.key == pygame.K_s:
                    slowcik.DOWN_KEY, slowcik.FACING_LEFT = True, True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    slowcik.RIGHT_KEY = False
                if event.key == pygame.K_a:
                    slowcik.LEFT_KEY = False
                if event.key == pygame.K_w:
                    slowcik.UP_KEY = False
                if event.key == pygame.K_s:
                    slowcik.DOWN_KEY = False
        bordery()
        draw_windows()
        # print(pygame.mouse.get_pos())
    pygame.quit()

if __name__ == "__main__":
    main()
