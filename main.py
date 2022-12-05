import pygame
import time
import const
from phisics.area import Area
from phisics.world import World
from actors.player_actor import PlayerActor
from actors.block_actor import BlockActor
from actors.time_actor import TimeActor
from rl.all_states import AllStates
from rl.player import Player


def run(all_states, situation=None):
    pygame.init()  # инициировали pygame
    pygame.font.init()
    # создали экран заданного размера
    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
    pygame.display.set_caption("Run")

    # получили объект твчающий за время
    clock = pygame.time.Clock()

    # инициировали спрайты (рисуемые объекты)
    world = World(all_states)

    all_sprites = pygame.sprite.Group()

    add_actor = lambda x: all_sprites.add(BlockActor(x))
#    remove_actor = lambda x: all_sprites.remove(x)
    #situation = [0, 1, 0, 0]
    area = Area(world, situation=situation, add_actor=add_actor)

    player = Player(4.5 * const.BLOCK_SIZE, const.HEIGHT - 2 * const.BLOCK_SIZE + 0.5 * const.PLAYER_HEIGHT, world)

    player_actor = PlayerActor(player)

    all_sprites.add(player_actor)

    time_actor = TimeActor(100, 50)
    all_sprites.add(time_actor)

    t1 = time.time()
    while world.running:
        clock.tick(const.FPS)  # держим частоту кадров не выше

        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                world.running = False

        # обновление
        t2 = time.time()
        dt = (t2 - t1)
        world.act(dt)
        player.act(dt)
        area.act(dt)
        all_sprites.update(dt=dt)

        t1 = t2
        # отрисовка
        screen.fill(const.BACKGROUND)
        all_sprites.draw(screen)
        pygame.display.flip()

    res = time_actor.time
    pygame.quit()
    return res


path = "D:/analitic/rl/run/"
fn = "v_eg_5b_g1_test.csv"
all_state = AllStates(AllStates.GREEDY)
all_state.readCSV(path+fn)
print('States count',len(all_state.states))
s = 0
n = 1
#situation = [0, 0, 0, 0, 2, 2]
for i in range(n):
    s += run(all_state)
    print('States count', len(all_state.states), 'reward = ', s / (i + 1))

# print(s/n)
#fn = "test_1.csv"
#all_state.saveCSV(path+fn)
