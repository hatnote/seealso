# -*- coding: utf-8 -*-

import Image
import argparse

SM_HEIGHT = 174
SM_WIDTH = 520
WIDTH_OFFSET = 80
WIDTH = 354


def main(filename, out_name):
    if not out_name:
        out_name = filename[:-4] + '_sm.png'
    large_img = Image.open(filename)
    small_img = large_img.resize((SM_WIDTH, SM_HEIGHT), Image.ANTIALIAS)
    crop_img = small_img.crop((WIDTH_OFFSET, 0, WIDTH_OFFSET + WIDTH, SM_HEIGHT))
    crop_img.save(out_name)
    print 'wrote', out_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='image filename')
    parser.add_argument('-o', '--output', help='filename to save the output',
                        default=None)
    args = parser.parse_args()
    main(args.filename, args.output)
