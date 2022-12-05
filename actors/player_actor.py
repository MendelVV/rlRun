import pygame
from phisics.bodyr import BodyR
import const


class PlayerActor(pygame.sprite.Sprite):
    DT = 0.1
    ACT_DT = 0.3
    ACTION_NONE = 0
    ACTION_WALK = 1
    ACTION_JUMP = 2

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.body = player.body

        self.dt = 0

        self.images = []
        path = 'resources/'
        fn = ['p1_walk1', 'p1_walk2', 'p1_jump1', 'p1_jump2']
        for nm in fn:
            image = pygame.image.load(path + nm + '.png')
            image = pygame.transform.scale(image, (const.PLAYER_WIDTH+2, const.PLAYER_HEIGHT+2))
            self.images.append(image)

        self.current_frame = 0
        self.image = self.images[self.current_frame]

        pos = self.body.getCenter()
        self.rect = pygame.Rect(pos[0]-1, pos[1]-1, const.PLAYER_WIDTH, const.PLAYER_HEIGHT)

    def update(self, dt):
        if self.body.action == BodyR.ACTION_RIGHT:
            self.dt += dt
            if self.dt >= PlayerActor.DT:
                self.current_frame = (self.current_frame + 1) % 2
                self.image = self.images[self.current_frame]
                self.dt = 0
        elif (self.body.action == BodyR.ACTION_JUMP) or (self.body.action == BodyR.ACTION_FALL):
            if self.body.velocity[1] < 0:
                self.image = self.images[2]
            else:
                self.image = self.images[3]

        x, y = self.body.getCenter()
        self.rect.center = (x-1, y-1)
        if x < -const.PLAYER_WIDTH/2 or y > const.HEIGHT + const.PLAYER_HEIGHT/2:
            self.player.world.running = False
