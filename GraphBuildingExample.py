import numpy as np
import math
N = 1000
M = 10
R = 5
class Event:
    def __init__(self, x, y, t, p):
        self.x = 0
        self.y = 0
        self.t = 0
        self.p = 0

def isWithin(event1, event2, radius, alpha=1, beta=1):
    x_i = event1.x
    x_j = event2.x
    y_i = event1.y
    y_j = event2.y
    t_i = event1.t
    t_j = event2.t
    spatial = abs(x_i - x_j) * abs(x_i - x_j) + abs(y_i - y_j) * abs(y_i - y_j)
    temporal = abs(t_i - t_j) * abs(t_i - t_j)
    return math.sqrt(alpha * spatial + beta * temporal) <= radius


def main():
    event = []  # M objects of Event class
    event.append(Event(1, 1, 1, -1))
    event.append(Event(1, 0, 2, 1))
    adMat = np.zeros([2, 2], dtype=int)
    print(adMat)
    for row in range(len(adMat)):
        for col in adMat[row]:
            if row == col:
              continue 
            if isWithin(event[row], event[col], R):
                adMat[row][col] = 1
                adMat[col][row] = 1
            else:
                adMat[row][col] = 0
                adMat[col][row] = 0
    print(adMat)
        
if __name__ == "__main__":
    main()
