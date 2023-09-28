import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY, self.FACING_LEFT = False, False, False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (665,350)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.velocity_x, self.velocity_y = 0, 0
        if self.LEFT_KEY:
            self.velocity_x = -5
            self.rect.x += self.velocity_x
        if self.RIGHT_KEY:
            self.velocity_x = 5
            self.rect.x += self.velocity_x
        if self.UP_KEY:
            self.velocity_y = -5
            self.rect.y += self.velocity_y
        if self.DOWN_KEY:
            self.velocity_y = 5
            self.rect.y += self.velocity_y
        self.set_state()
        self.animate()

    def set_state(self):
        self.state = 'idle'
        if self.velocity_x < 0 and self.velocity_y < 0:
            self.state = 'moving left'
        elif self.velocity_x > 0 or self.velocity_y < 0:
            self.state = 'moving right'
        elif self.velocity_x < 0 or self.velocity_y > 0:
            self.state = 'moving left'
        

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == 'idle':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_right[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_left[self.current_frame]


    def load_frames(self):
        self.idle_frames_left = [pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_0_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_1_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_2_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_3_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_4_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_5_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_6_delay-0.1s.gif').convert(), (125,110)),
                                 pygame.transform.scale(pygame.image.load('SiemaSlowLife/dino_idle/frame_7_delay-0.1s.gif').convert(), (125,110))]
        self.walking_frames_left = [pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_0.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_1.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_2.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_3.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_4.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_5.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_6.png').convert(), (125,110)),
                                    pygame.transform.scale(pygame.image.load('SiemaSlowLife\dino_walk\dino_7.png').convert(), (125,110))]
        self.idle_frames_right = []
        for frame in self.idle_frames_left:
            self.idle_frames_right.append(pygame.transform.flip(frame, True, False))
        self.walking_frames_right = []
        for frame in self.walking_frames_left:
            self.walking_frames_right.append(pygame.transform.flip(frame, True, False))