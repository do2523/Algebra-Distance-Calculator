import math

# distance formula


def dist(p1, p2):
    return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)


def distance(points):
    # vars
    minimum_distance = float("inf")
    p1 = 0
    p2 = 0
    # nested for loop to go through each point
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = dist(points[i], points[j])
            if distance < minimum_distance:
                minimum_distance = distance
                p1 = points[i]
                p2 = points[j]
    return p1, p2, minimum_distance


print(distance([(1, 2), (4, 6)]))
