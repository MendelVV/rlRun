import time
import const
from phisics.area import Area
from phisics.world import World
from rl.player import Player
from rl.state import make_situation


def run(all_states, situation=None, mx=1200):
    world = World(all_states)

    if situation is not None:
        area = Area(world, make_situation(situation, const.REVIEW+1))
    else:
        area = Area(world)
    player = Player(4.5 * const.BLOCK_SIZE, const.HEIGHT - 2 * const.BLOCK_SIZE + 0.5 * const.PLAYER_HEIGHT, world)

    all_time = 0
    t_start = time.time()
    k = 0
    step = 0.013
    while world.running and mx > all_time:
        # обновление
        dt = step
        world.act(dt)
        player.act(dt)
        area.act(dt)
        all_time += dt
        k += 1
    dt = time.time() - t_start

    return round(dt, 4), round(step*k,2)