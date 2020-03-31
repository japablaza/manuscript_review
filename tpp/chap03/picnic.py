#!/usr/bin/env python3
"""Comida para el picnic"""

import argparse


def get_args():
    """Argumentos desde el CLI"""
    parse = argparse.ArgumentParser(
        description='Lista de comida',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parse.add_argument('platos',
                       metavar='texto',
                       nargs='+',
                       help='Plato(s) para el picnic')

    parse.add_argument('-o',
                       '--ordenados',
                       action='store_true',
                       help='Ordena los platos en la lista')

    return parse.parse_args()


def main():
    """La funcion principal"""

    argumentos = get_args()
    platos = argumentos.platos
    numero = len(platos)

    if argumentos.ordenados:
        platos.sort()

    traen = ''
    if numero == 1:
        traen = platos[0]
    elif numero == 2:
        traen = ' y '.join(platos)
    else:
        platos[-1] = 'y ' + platos[-1]
        traen = ', '.join(platos)

    print(f'Tu traes {traen}.')


if __name__ == '__main__':
    main()
