#!/usr/bin/env python3
"""
Who: Jose Apablaza
What: Simple codigo 'Hello, Worlds!' usando argparse
"""
# What: Say Hello!

import argparse


def argumentos():
    """Obtener argumentos desde cli"""
    parse = argparse.ArgumentParser(description='Di Hola')
    parse.add_argument('-n', '--name', metavar='name', default='Mundo',
                       help='Nombre a quien saludar')
    return parse.parse_args()


def main():
    """Llamando la funcion para pasar argumentos"""
    argus = argumentos()
    print('Hola, ' + argus.name + '!')


if __name__ == '__main__':
    main()
