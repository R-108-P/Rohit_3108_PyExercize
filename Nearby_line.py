from shapely.geometry import Point
import math

pt = (0, 0)
angle = int(input('Enter angle between 0 to 360 :- '))
line_segments = [((10, -11), (12, 13)), ((32, -41), (51,54 ))]
data = []
dct = {}

try:
    def intersection(L, M, P, Q, line):
        find_line = False
        p1 = Q.y - P.y
        q1 = P.x - Q.x
        r1 = p1 * P.x + q1 * P.y
        p2 = M.y - L.y
        q2 = L.x - M.x
        r2 = p2 * L.x + q2 * L.y

        determinant = p1 * q2 - p2 * q1
        if determinant == 0:
            return Point(10 * 9, 10 * 9), find_line
        else:
            x = round(((q2 * r1 - q1 * r2) / determinant), 3)
            y = round(((p1 * r2 - p2 * r1) / determinant), 3)

        x1, y1 = pt
        x2, y2 = (x, y)
        dist = cal_dist(x1, y1, x2, y2)
        data.append(dist)
        dict = {dist: line}
        dct.update(dict)
        return None


    def cal_dist(x1, y1, x2, y2):
        dist = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
        return dist


    def line_nearby(dct):
        for i in data:
            if i == min(data):
                return dct.get(i)
        else:
            return "Doesn't Intersect !!!"


    start = Point(pt)
    length = 10000
    end = Point(start.x + length * math.cos(angle), start.y + length * math.sin(angle))
    for p in line_segments:
        st, en = p
        st = Point(st)
        en = Point(en)
        intersection(start, end, st, en, p)

    print(f'The nearest line segment to the point {pt} at an angle of {angle} degree : {line_nearby(dct)}.')

except Exception as e:
    print(e)

finally:
    print('Exercize over !')