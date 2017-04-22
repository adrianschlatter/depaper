# -*- coding: utf-8 -*-
"""
depaper command-line tool
"""

from argparse import ArgumentParser
from . import depaper
from matplotlib.pyplot import imread, imsave
from matplotlib.cm import gray as cmgray


def cli():
    parser = ArgumentParser()
    parser.add_argument("imagename", help="image to be depapered")
    parser.add_argument("outputfilename", help="output filename")
    parser.add_argument("--outfmt", default=None, help="output file format")
    args = parser.parse_args()

    img = imread(args.imagename)
    depapered = depaper(img)
    imsave(args.outputfilename, depapered, vmin=0, vmax=1, cmap=cmgray,
           format=args.outfmt)


if __name__ == '__main__':
    cli()
