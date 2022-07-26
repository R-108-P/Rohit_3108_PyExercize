import math
import sys
from sys import exit
import matplotlib.pyplot as plt
import numpy as np


def intersect() -> bool:
    intersection = False

    input_pt = input("Enter Point co-ordinates")
    if len(input_pt) != 3:
        print("Point can only have 2 coordinates.")
        exit()

    test_point = tuple(int(xy) for xy in input_pt.split(","))
    t1, t2 = test_point
    t1 = float(t1)
    t2 = float(t2)
    print(t1, t2)

    inp_angle = int(input("Please enter an angle between 0 and 360: "))
    if not 0 <= inp_angle <= 360:
        print("An angle cannot be outside 0-360 range")
        exit()

    num = 0
    tst_line = []
    while True:
        in_line_segs = str(input("Provide a line by providing coordinates as x1,y1,x2,y2  OR 'Done' when you have entered all lines you want: "))

        if num == 0 and (in_line_segs == "Done" or in_line_segs == 'done'):
            print("Enter coordinates of line segments")
            break
        if len(in_line_segs) >= 12 and (in_line_segs != 'done' and in_line_segs != "Done"):
            print("Please make sure you have entered coordinates as x1,y1,x2,y2 with no spaces")
            break

        if in_line_segs == "Done" or in_line_segs == 'done':
            print(f'{num} lines captured')
            break

        if num == 1 and (in_line_segs == "Done" or in_line_segs == 'done'):
            print(f'Only one line entered, note that {tst_line[0]} line will be the closest to the line from test 'f'point, ''if they intersect')
            break

        test_line = tuple(int(xii) for xii in in_line_segs.split(","))
        tst_line.append(test_line)
        num += 1

    dct = {}
    plt.plot(t1, t2)
    plt.text(t1 - 0.5, t2 - 0.5, f'TestPt{t1},{t2}')

    if 0 <= inp_angle <= 90 or 271 <= inp_angle <= 360:

        plt.text(t1, t2 - 0.9, 'θ=' + str(inp_angle))
        m = np.tan(np.radians(inp_angle))
        x_coord = np.array(range(int(t1), 101, +1))
        y_intersect = t2 - (m * t1)
        y_coord = np.array(m * (x_coord) + y_intersect)
        plt.plot(x_coord, y_coord)

    if 91 <= inp_angle <= 270:

        plt.text(t1, t2 - 0.9, 'θ=' + str(inp_angle))
        m = np.tan(np.radians(inp_angle))
        print(m)
        x_coord = np.array(range(int(t1), -101, -1))
        print(x_coord)
        y_intersect = t2 - (m * t1)
        print(y_intersect)
        y_coord = np.array((m * x_coord) + y_intersect)
        print(y_coord)
        plt.plot(x_coord, y_coord)

    for itr in range(len(tst_line)):
        print(tst_line[itr])
        x1, y1, x2, y2 = tst_line[itr]

        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)

        plt.text(x1, y1 - 0.8, 'A(%s,%s)' % (x1, y1))
        plt.text(x2, y2 - 0.4, 'B(%s,%s)' % (x2, y2))

        plt.plot((x1, x2), (y1, y2))


        m = float((y2 - y1) / (x2 - x1))
        y_intersect_line = float(y1 - (m * x1))


        xi = (y_intersect - y_intersect_line) / (m - m)
        yi = (m * xi) + y_intersect_line


        if min(x_coord) < xi < max(x_coord) and min(y_coord) < yi < max(y_coord):
            intersection = True
        else:
            print(
                f"{tst_line[itr]} line do not intersect with line projected from the test point({t1, t2}) at given "
                f"angle of {inp_angle} degrees")

        if intersection == True:
            dist = round(math.sqrt(((t1 - xi) ** 2) + ((t2 - yi) ** 2)), 2)
            print(dist)
            dct[dist] = tst_line[itr]
    print(dct)


    list_distance = list(dct.keys())
    min_val = min(list_distance)
    print(
        f"the line that is nearest to the test point ({t1},{t2}) is {dct[min_val]} and it is {min_val} distance away at "
        f"an angle of {inp_angle} degrees\n "
        f"The lines intersect at ({xi, yi})")

    plt.xlim(-6, 5)
    plt.ylim(-11, 15)

    plt.xlabel("x co-ordinates")
    plt.ylabel("y co-ordinates")

    plt.grid()

    plt.show()
    return intersection


print(intersect())

