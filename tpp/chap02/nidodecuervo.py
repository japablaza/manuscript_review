#!/usr/bin/env python3
"""
Who     : Jose Apablaza
When    : 2020-03-30
What    : Argumento de posicion
"""

import argparse
# import os
# import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Elige el articulo correcto',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('palabra',
                        metavar='palabra',
                        help='Una sola palabra')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Dale y corre tu codigo"""

    args = get_args()
    pal = args.palabra
    articulo = 'an' if pal[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Capitan, {articulo} {pal} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
