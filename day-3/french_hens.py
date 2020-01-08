import math
from paths import wire_1_path, wire_2_path


def _get_wire_coords_from_path(wire_path):
    coords = [[0, 0]]
    latest = [0, 0]
    for instruction in wire_path:
        if 'R' in instruction or 'L' in instruction:
            if 'R' in instruction:
                latest[0] += int(instruction[1:])
            else:
                latest[0] -= int(instruction[1:])
            coords.append(latest[:])
        elif 'U' in instruction or 'D' in instruction:
            if 'U' in instruction:
                latest[1] += int(instruction[1:])
            else:
                latest[1] -= int(instruction[1:])
            coords.append(latest[:])
    return coords


wire_1_coords = _get_wire_coords_from_path(wire_1_path)
wire_2_coords = _get_wire_coords_from_path(wire_2_path)


def _get_intersection(before_1, after_1, before_2, after_2):
    if (before_1[0] > before_2[0] and before_1[0] < after_2[0]) \
       or (before_1[0] < before_2[0] and before_1[0] > after_2[0]):
        if (before_2[1] > before_1[1] and before_2[1] < after_1[1]) \
           or (before_2[1] < before_1[1] and before_2[1] > after_1[1]):
            return [before_1[0], before_2[1]]
    if (before_2[0] > before_1[0] and before_2[0] < after_1[0]) \
       or (before_2[0] < before_1[0] and before_2[0] > after_1[0]):
        if (before_1[1] > before_2[1] and before_1[1] < after_2[1]) \
           or (before_1[1] < after_2[1] and before_1[1] > before_2[1]):
            return [before_2[0], before_1[1]]


def _find_intersections(coords_1, coords_2):
    intersections = []
    for i in range(len(coords_1)):
        if i == 0:
            continue
        before_1 = coords_1[i-1]
        after_1 = coords_1[i]
        for j in range(len(coords_2)):
            if j == 0:
                continue
            before_2 = coords_2[j-1]
            after_2 = coords_2[j]
            intersection = _get_intersection(before_1, after_1, before_2, after_2)  # noqa e501

            if intersection and intersection != [0, 0]:
                intersections.append(intersection)
    return intersections


def _find_closest(intersections):
    closest = math.inf
    for ints in intersections:
        distance = abs(ints[0]) + abs(ints[1])
        if distance < closest:
            closest = distance

    return closest


intersections = _find_intersections(wire_1_coords, wire_2_coords)
closest_distance = _find_closest(intersections)
print(closest_distance)
