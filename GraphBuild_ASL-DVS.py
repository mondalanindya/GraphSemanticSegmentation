import math
import numpy
N = 1000
M = 10
R = 5
class Event:
    def __init__(self):
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
    adMat = numpy.zeros([M, M], dtype=int)
    for row in range(len(adMat) - 1):
        for col in adMat[row]:
            if isWithin(event[row], event[col], R):
                adMat[row][col] = 1
                adMat[col][row] = 1
            else:
                adMat[row][col] = 0
                adMat[col][row] = 0
    print(adMat)
        
if __name__ == "__main__":
    main()
