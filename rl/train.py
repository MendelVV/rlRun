import const
from rl.all_states import AllStates
from rl.check import check_by_situations
from rl.run import run
from rl.state import make_situation


def train_by_states(all_states=None, n=100, state=None):
    if all_states is None:
        all_states = AllStates(AllStates.RANDOM)
    if state is None:
        start = 0
        st = (const.BLOCK_TYPES+1) ** (const.REVIEW + 1)
    else:
        start = state
        st = state+1
    print(start, st, 'total states', st-start)
    for i in range(start, st):
        for j in range(n):
            dt = run(all_states, i)
#            print(i, j, 'dt =', dt, 'states =', len(all_states.states))
#        print('check!')
        r = check_by_situations(all_states, situation=i)
        print("state", i, make_situation(i, const.REVIEW+1), " reward", r)
    return all_states


def train_by_states_v2(all_states=None):
    if all_states is None:
        all_states = AllStates(AllStates.RANDOM)
    start = 0
    st = (const.BLOCK_TYPES+1) ** (const.REVIEW + 1)
    print(start, st, 'total situations', st-start)

    for j in range(200):
        dt = run(all_states, 0)
    mx = check_by_situations(all_states, situation=0)[0]
    print('mx', mx)

    for i in range(start, st):
        r = check_by_situations(all_states, situation=i)[0]
        steps = 0
        while abs(r-mx) > 0.1*mx:
            for j in range(100):
                dt = run(all_states, i)
            steps += 1
            r = check_by_situations(all_states, situation=i)[0]
            print("state", i, make_situation(i, const.REVIEW+1), 'reward', r, 'steps ', steps)
    return all_states


def train_random(all_states=None, n=1000):
    if all_states is None:
        all_states = AllStates(AllStates.GREEDY)
    for i in range(n):
        dt = run(all_states)
        print(i, 'dt =', dt, 'states =', len(all_states.states))
    return all_states


path = "D:/analitic/rl/run/"
fn = "v_r_3s_test.csv"

#all_st = train_by_states_v2()

all_st = AllStates(AllStates.EPSILON_GREEDY)
all_st.readCSV(f_name=path+fn)
print('States count', len(all_st.states))

#all_st = train_by_states(all_states=all_st, n=200, state=62)
mx = check_by_situations(all_st, 0)[0]
n = (const.BLOCK_TYPES+1) ** (const.REVIEW + 1)
for i in range(1, n):
    r = check_by_situations(all_st, i)[0]
    print('state', i, 'reward', r)
    if abs(mx-r) > 4:
        all_st = train_by_states(all_states=all_st, n=100, state=i)
        r = check_by_situations(all_st, i)

#all_st = AllStates(AllStates.EPSILON_GREEDY)
#all_st = train_random(all_states=all_st, n=1000)
#r = check_by_situations(all_st)
#print('dr', 100*(max(r)-min(r))/r[0], max(r), min(r))

fn = "v_r_3s_test_add.csv"
all_st.saveCSV(path + fn)
