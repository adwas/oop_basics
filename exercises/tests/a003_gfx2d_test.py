# pylint: disable=C0111

import unittest
from typing import List
from src import gfx2d


class TestGFX2dCase(unittest.TestCase):

    def test_point_class_int_constructor(self):
        point = gfx2d.Point2d(12, 32)
        self.assertEqual(point.x_cord, 12)
        self.assertEqual(point.y_cord, 32)

    def test_point_class_point_constructor(self):
        point1 = gfx2d.Point2d(12, 32)
        point = gfx2d.Point2d.from_point(point1)
        self.assertEqual(point.x_cord, 12)
        self.assertEqual(point.y_cord, 32)

    def test_point_distanse_calculation(self):
        '''
            see: https://www.mathsisfun.com/algebra/distance-2-points.html
            p1 = (xa,ya), p2 = (xb,yb)
            distance = sqrt((xa-xb)^2+(ya-yb)^2)

            lets round it with an accuracy of up to thousandth (0.001)
        '''
        point1 = gfx2d.Point2d(9, 7)
        point2 = gfx2d.Point2d(3, 2)

        distance = point1.distance_to(point2)
        self.assertEqual(distance, 7.81)

    def test_color_class(self):
        color = gfx2d.RgbColor(255, 0, 1)
        self.assertEqual(color.r_color, 255)
        self.assertEqual(color.g_color, 0)
        self.assertEqual(color.b_color, 1)

    def test_pixel_class(self):
        point = gfx2d.Point2d(9, 7)
        color = gfx2d.RgbColor(255, 0, 1)
        pixel = gfx2d.Pixel(point, color)
        self.assertEqual(pixel.point, gfx2d.Point2d(9, 7))
        self.assertEqual(pixel.color, gfx2d.RgbColor(255, 0, 1))
        self.assertEqual(pixel, gfx2d.Pixel.from_ints(9, 7, 255, 0, 1))

    def test_pixel_class_to_string(self):
        pixel = gfx2d.Pixel.from_ints(9, 7, 255, 0, 1)
        pixel_str = "%s" % pixel
        self.assertEqual(pixel_str, "Pixel(p=(9,7),c=(255,0,1))")

    def test_line_class(self):
        point1 = gfx2d.Point2d(9, 7)
        point2 = gfx2d.Point2d(3, 2)
        color = gfx2d.RgbColor(255, 5, 4)
        line = gfx2d.Line(point1, point2, color)
        self.assertEqual(line.start_point, gfx2d.Point2d(9, 7))
        self.assertEqual(line.end_point, point2)
        self.assertEqual(line.color, color)

    def test_draw_line_method(self):
        # https://en.wikipedia.org/wiki/Line_drawing_algorithm
        point1 = gfx2d.Point2d(3, 2)
        point2 = gfx2d.Point2d(9, 7)
        color = gfx2d.RgbColor(255, 5, 4)
        line = gfx2d.Line(point1, point2, color)
        pixels: List[gfx2d.Pixel] = line.create_pixels()

        pixels_to_check: List[gfx2d.Pixel] = [
            gfx2d.Pixel.from_ints(3, 2, 255, 5, 4),
            gfx2d.Pixel.from_ints(4, 2, 255, 5, 4),
            gfx2d.Pixel.from_ints(5, 3, 255, 5, 4),
            gfx2d.Pixel.from_ints(6, 4, 255, 5, 4),
            gfx2d.Pixel.from_ints(7, 5, 255, 5, 4),
            gfx2d.Pixel.from_ints(8, 6, 255, 5, 4),
            gfx2d.Pixel.from_ints(9, 7, 255, 5, 4)]

        self.assertListEqual(pixels, pixels_to_check)
