import pygame
from phisics.rectangle import Rectangle
from phisics.bodyr import BodyR
import const


class TimeActor(pygame.sprite.Sprite):

    WIDTH = 200
    HEIGHT = 50

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.time = 0
        self.text = 'Time = '+str(self.time)
        self.size = 36
        self.font = pygame.font.SysFont("Arial", self.size)
        self.textSurf = self.font.render(self.text, True, const.BLACK)
        self.image = pygame.Surface((TimeActor.WIDTH, TimeActor.HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [TimeActor.WIDTH/ 2 - W / 2, TimeActor.HEIGHT / 2 - H / 2])
        self.rect.center = (x, y)

    def update(self, dt):
        self.time += dt
        self.text = 'Time = '+str(round(self.time,1))
        self.textSurf = self.font.render(self.text, False, const.BLACK)
        self.image = pygame.Surface((TimeActor.WIDTH, TimeActor.HEIGHT), pygame.SRCALPHA)
        #self.rect = self.image.get_rect()
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [TimeActor.WIDTH/ 2 - W / 2, TimeActor.HEIGHT / 2 - H / 2])