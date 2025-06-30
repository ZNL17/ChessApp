import vector
import numpy as np


class Pieces:
    def __init__(self):
        pass

    def directionTemplate(dis_vec, start, field):
        xoff = (abs(dis_vec[0]) // dis_vec[0]) if dis_vec[0] != 0 else 0
        yoff = (abs(dis_vec[1]) // dis_vec[1]) if dis_vec[1] != 0 else 0
        for _ in range(0, np.max(np.abs(dis_vec))):
            if field[start.v[0] + xoff][start.v[1] + yoff] != "":
                return False
            xoff += 1 * (abs(xoff) // xoff) if xoff != 0 else 0
            yoff += 1 * (abs(yoff) // yoff) if yoff != 0 else 0
        return True

    def straight(dis_vec, start, field):
        if dis_vec.tolist().count(0) % 2:
            return Pieces.directionTemplate(dis_vec, start, field)
        else:
            return False

    def cross(dis_vec, start, field):
        if dis_vec.tolist().count(0) == 0 and abs(dis_vec[0]) == abs(dis_vec[1]):
            return Pieces.directionTemplate(dis_vec, start, field)
        else:
            return False

    def jump(dis_vec, start, field):
        print("dis_vec: ", dis_vec)
        if abs(dis_vec[0]) in [1, 2] and abs(dis_vec[1]) in [1, 2]:
            if (
                abs(dis_vec[0]) / abs(dis_vec[1]) in [0.5, 2.0]
                or abs(dis_vec[0]) + abs(dis_vec[1]) == 3
            ):
                return True
            else:
                return False
        else:
            return False

    def step(dis_vec, start, field):
        print("dis_vec: ", dis_vec)
        print("field[start.v[0]][start.v[1]][:1]: ", field[start.v[0]][start.v[1]][:1])
        if field[start.v[0]][start.v[1]][:1] == "W":
            if dis_vec.tolist() == [-1, 0]:
                return True
            else:
                return False
        else:
            if dis_vec.tolist() == [1, 0]:
                return True
            else:
                return False

    def allStep(dis_vec):
        pass

    def both(dis_vec, start, field):
        if dis_vec.tolist().count(0) % 2:
            return Pieces.directionTemplate(dis_vec, start, field)
        if dis_vec.tolist().count(0) == 0 and abs(dis_vec[0]) == abs(dis_vec[1]):
            return Pieces.directionTemplate(dis_vec, start, field)
        return False
