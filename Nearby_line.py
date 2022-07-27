from shapely.geometry import Point
import math

pt = (0, 0)
angle = int(input('Enter angle between 0 to 360 :- '))
line_segments = [((10, -11), (12, 13)), ((32, -41), (51,54 ))]
data = []
dct = {}

try:
    def origin_lineseg_dist(pt1, pt2) -> tuple[list, float] | None:
        p = pt2[1] - pt1[1]
        q = pt2[0] - pt1[0]

        if (p == 0 and angle == 0) or (angle == 90 and q == 0):
            return None

        elif q != 0:
            m = p / q  # y = mx + c , m is slope

            r = pt1[1] - (m * pt1[0])
            m_start_pt = math.tan(math.radians(angle))
            x_coord = round(r / (m_start_pt - m), 3)
            y_coord = round(m * x_coord + r, 3)

        else:
            x_coord = pt1[0]
            m_start_pt = (math.tan(math.radians(angle)))
            y_coord = m_start_pt * x_coord

        if min(pt1[0], pt2[0]) <= x_coord <= max(pt1[0], pt2[0]) and min(pt1[1], pt2[1]) <= \
                y_coord <= max(pt1[1], pt2[1]):
            return [pt1, pt2], round(math.dist((0, 0), (x_coord, y_coord)))


    print(origin_lineseg_dist((2.0, 3.0),(4.0,5.0)))

    print(f'The nearest line segment to the point {pt} at an angle of {angle} degree : {origin_lineseg_dist((1,2),(3,4))}.')

except Exception as e:
    print(e)

finally:
    print('Exercize over !')