from rl.all_states import AllStates
import const
from rl.run import run
from rl.state import make_situation


def check_by_situations(all_states, situation=None):
    res = []
    type = all_states.type
    static = all_states.static
    all_states.type = AllStates.GREEDY
    all_states.static = True
    if situation is None:
        start = 0
        st = (const.BLOCK_TYPES+1) ** (const.REVIEW + 1)
    else:
        start = situation
        st = situation + 1
    for i in range(start, st):
       # print('check', i)
        dt = run(all_states, situation=i)
        res.append(dt[-1])
#        print('GREEDY', i, 'dt =', dt, 'situation', make_situation(i, const.REVIEW + 1))
    all_states.type = type
    all_states.static = static
    return res