import random
from typing import NamedTuple

import numpy as np
from PIL import Image


class Point(NamedTuple):
    x: int
    y: int


class Rectangle(NamedTuple):
    ul: Point
    lr: Point


class Triangle(NamedTuple):
    p0: Point
    p1: Point
    p2: Point


class Line(NamedTuple):
    p0: Point
    p1: Point


class Polygon:

    def __init__(self, points: [Point]):
        self.points: [Point] = points


class Circle(NamedTuple):
    center: Point
    radius: int


# Point = collections.namedtuple("Point", ["x", "y"])
# Rectangle = collections.namedtuple("Rectangle", ["ul", "lr"])
# Triangle = collections.namedtuple("Triangle", ["p1", "p2", "p3"])


def set_pixel(_img: [[[int, int, int]]], x: int, y: int, val: [int, int, int]):
    _img[x, y] = val


def bounding_box(points: [Point]) -> Rectangle:
    ul = Point(points[0].x, points[0].y)
    lr = Point(points[0].x, points[0].y)
    for p in points:
        if p.x < ul.x:
            ul = Point(p.x, ul.y)
        if p.x > lr.x:
            lr = Point(p.x, lr.y)
        if p.y < ul.y:
            ul = Point(ul.x, p.y)
        if p.y > lr.y:
            lr = Point(lr.x, p.y)
    return Rectangle(ul, lr)


def draw_rectangle(_img, rect: Rectangle, val):
    for i in range(0, rect.lr.y):
        for j in range(0, rect.lr.x):
            set_pixel(_img, i + rect.ul.x, j + rect.ul.y, val)


def point_vs_edge(p: Point, edge: Line):
    p1, p2 = edge
    result = (p.x - p1.x) * (p2.y - p1.y) - (p.y - p1.y) * (p2.x - p1.x)
    return result


def is_point_inside_triangle(p: Point, t: Triangle):
    return point_vs_edge(p, Line(t.p0, t.p1)) >= 0 and \
           point_vs_edge(p, Line(t.p1, t.p2)) >= 0 and \
           point_vs_edge(p, Line(t.p2, t.p0)) >= 0 or \
           point_vs_edge(p, Line(t.p0, t.p1)) <= 0 and \
           point_vs_edge(p, Line(t.p1, t.p2)) <= 0 and \
           point_vs_edge(p, Line(t.p2, t.p0)) <= 0


def draw_triangle(_img, triangle: Triangle, val):
    box = bounding_box([*triangle])
    # print(box)
    for i in range(box.ul.x, box.lr.x):
        for j in range(box.ul.y, box.lr.y):
            if is_point_inside_triangle(Point(i, j), triangle):
                _img[j, i] = val


def prepare_img(size, rand_gen=False):
    pixels = np.zeros((size, size, 3), dtype='uint8')
    if rand_gen:
        for i in range(size):
            for j in range(size):
                r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                pixels[i, j] = [r, g, b]
    return pixels


def clear_screen(scr):
    return scr.fill(0)


def draw_polygon(_img, poly: Polygon, val):
    if len(poly.points) > 3:
        draw_triangle(_img, Triangle(poly.points[0], poly.points[1], poly.points[2]), val)
        del poly.points[1]
        draw_polygon(_img, poly, val)
    else:
        draw_triangle(_img, Triangle(*poly.points), val)


def manhattan_dist(p1: Point, p2: Point):
    return pow(abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2, 1 / 2)


def draw_circle(_img, circ: Circle, val):
    b_box = [Point(circ.center.x - circ.radius, circ.center.y - circ.radius),
             Point(circ.center.x + circ.radius, circ.center.y + circ.radius)]
    rect = bounding_box(b_box)
    for i in range(0, rect.lr.y):
        for j in range(0, rect.lr.x):
            x, y = i + rect.ul.x, j + rect.ul.y
            if manhattan_dist(circ.center, Point(x, y)) < circ.radius:
                set_pixel(_img, x, y, val)


if __name__ == "__main__":
    img = prepare_img(200, True)
    # draw_rectangle(img, Rectangle(Point(10, 10), Point(10, 50)), [255, 255, 0])
    draw_triangle(img, Triangle(Point(0, 0), Point(100, 0), Point(100, 100)), [0, 255, 255])
    draw_triangle(img, Triangle(Point(100, 0), Point(100, 100), Point(200, 0)), [0, 255, 0])
    # random_triangle = Triangle(
    #     Point(random.randrange(0, 200), random.randrange(0, 200)),
    #     Point(random.randrange(0, 200), random.randrange(0, 200)),
    #     Point(random.randrange(0, 200), random.randrange(0, 200))
    # )
    # print(random_triangle)
    # draw_triangle(img, random_triangle, [0, 255, 0])
    draw_polygon(img,
                 Polygon([Point(20, 60), Point(40, 50), Point(60, 70), Point(60, 100), Point(40, 120), Point(20, 100)]),
                 [255, 255, 0])
    draw_circle(img, Circle(Point(150, 150), 40), [255, 0, 255])
    screen = Image.fromarray(img, 'RGB')
    screen.show()


class Test:
    test1: str
    test3: int

    def __init__(self, test1: str, test3: int):
        self.test1: str = test1
        self.test3: int = test3
