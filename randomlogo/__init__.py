#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import cairo
import os
import rsvg

from jinja2 import Environment, FileSystemLoader
from PIL import Image
from random import choice, randrange

dirname, filename = os.path.split(os.path.abspath(__file__))
env = Environment(
    loader=FileSystemLoader(os.path.join(dirname, "templates/")))


def xml2pil(xml, width, height):
    """ Takes an SVG as input, renders via cairo and returns it as a PIL image
    """
    # http://stackoverflow.com/questions/6589358/convert-svg-to-png-in-python
    # http://cairographics.org/pythoncairopil/
    handle = rsvg.Handle(None, xml)
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    handle.render_cairo(context)
    return Image.frombuffer('RGBA', (width, height), surface.get_data(), 'raw',
                            'RGBA', 0, 1)


def generar_logo(colores, size=400):

    template = env.get_template("escudos.jinja2")
    shapes = ["cicle", "rect"]
    circles = []
    rects = []

    for color in colores:
        shape = choice(shapes)
        stroke = randrange(1, 10)
        if shape == "rect":
            x = randrange(-50, 350)
            y = randrange(-50, 350)
            width = randrange(100, 200)
            height = randrange(100, 200)
            rects.append((color, x, y, width, height, stroke))
        else:
            cx = randrange(100, 200)
            cy = randrange(100, 200)
            r = randrange(60, 150)

            circles.append((color, cx, cy, r, stroke))

    data = {"circles": circles,
            "rects": rects}

    xml = template.render(**data)
    return xml2pil(xml, size, size)


def main():
    parser = argparse.ArgumentParser(
        description="Generador de logos")
    parser.add_argument("colores", help="colores")
    parser.add_argument("--output", "-o", help="output file",
                        default="logo.png")
    args = parser.parse_args()
    image = generar_logo(args.colores.split(","))
    image.save(args.output)

if __name__ == '__main__':
    image = generar_logo(["#aabbcc", "#ff00aa"])
    image.save("logo.png")
