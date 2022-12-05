import pygame
import const


class BlockActor(pygame.sprite.Sprite):

    SIZE = 30

    def __init__(self, block):
        pygame.sprite.Sprite.__init__(self)
        self.block = block
        image = pygame.image.load("resources/grass.png")
        self.image = pygame.transform.scale(image, (BlockActor.SIZE, BlockActor.SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = self.block.body.getCenter()

    def update(self, dt):
        self.rect.center = self.block.body.getCenter()
        if self.rect.center[0] < -const.BLOCK_SIZE:
            self.kill()