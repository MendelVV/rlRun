import const


def make_situation(n, sz):
    d = const.BLOCK_TYPES+1
    res = [0]*sz
    for i in range(sz):
        r = n % d
        res[sz-i-1] = r
        n = n//d
    return res


def get_state_1(p, b, a):
    # генерируем кортеж состояния+действие
    # состояние - положение человечка по y
    # состояние - положение следующего блока по y
    # расстояние от человечка до следующего блока
    # действие - одно из возможных (идти или прыгнуть)
    # p - центр человечка
    # b - центр блока
    # a - действие
    dx = int(b[0] - p[0])
    state = (int(p[1]), int(b[1]), dx, a)
    return state


def get_state_many(p, blocks, a):
    # генерируем кортеж состояния+действие
    # состояние - положение человечка по y
    # состояние - положение следующего блока по y
    # расстояние от человечка до следующего блока
    # действие - одно из возможных (идти или прыгнуть)
    # p - центр человечка
    # bloks - список следующих блоков
    # a - действие
    res = [int(p[1])]
    for block in blocks:
        b = block.getCenter()
        dx = int(b[0] - p[0])
        res.append(int(b[1]))
        res.append(dx)
    res.append(a)
    state = tuple(res)
    return state

def get_state_many_2(p, blocks, a):
    # генерируем кортеж состояния+действие
    # состояние - положение человечка по y
    # состояние - положение следующего блока по y
    # расстояние от человечка до следующего блока
    # действие - одно из возможных (идти или прыгнуть)
    # p - центр человечка
    # bloks - список следующих блоков
    # a - действие
    res = [int(p[1])]
    for block in blocks:
        b = block.getCenter()
        dx = int(b[0] - p[0])//2
        res.append(int(b[1]))
        res.append(dx)
    res.append(a)
    state = tuple(res)
    return state