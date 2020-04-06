#!/usr/bin/env python3

import argparse


def argu_cli():
    """Aqui la magia de argparse"""
    pedir = argparse.ArgumentParser(
        description='Leer la primare letra de la linea',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    pedir.add_argument('letra',
                       help='Letras de cada linea',
                       metavar='texto',
                       nargs='+',
                       type=str)

    pedir.add.argument('-a',
                       '--archivo',
                       help='Archivo en el directorio',
                       metavar='Archivo de texto',
                       type=argparse.FileType('r'),
                       default='text.txt')

    return pedir.parse_args()




def main():
    """Aqui llamamos la funcion argu_cli"""


if __name__ == '__main__':
    main()
