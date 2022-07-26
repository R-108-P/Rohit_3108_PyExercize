from shapely.geometry import Point
import math

pt = (0, 0)
angle = 0
line_segments = [((5, -7), (6, 6)), ((8, -4), (3, 2))]
data = []
dct = {}

def origin_lineseg_dist(pt1, pt2) -> tuple[list, float] | None:
    p = pt2[1] - pt1[1]
    q = pt2[0] - pt1[0]

    if (p == 0 and angle == 0) or (angle == 90 and q == 0):
        return
    elif q != 0:
        m = p / q  # y = mx + c , m is slope

        r = pt1[1] - (m * pt1[0])
        m_start_pt = math.tan(math.radians(angle))
        x_coord = round(r / (m_start_pt - m), 3)
        y_coord = round(m * x_coord + r, 3)

    else:
        x_coord = pt1[0]  # x1
        m_start_pt = (math.tan(math.radians(angle)))
        y_coord = m_start_pt * x_coord

    if min(pt1[0], pt2[0]) <= x_coord <= max(pt1[0], pt2[0]) and min(pt1[1], pt2[1]) <= \
            y_coord <= max(pt1[1], pt2[1]):
        return [pt1, pt2], round(math.dist((0, 0), (x_coord, y_coord)))
    
print(origin_lineseg_dist((2.0,3.0),(3.0,8.0)))
print(f'The line segment that is closest to the point {pt} at {angle} degrees is : {origin_lineseg_dist(dct)}.')
