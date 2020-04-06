#!/usr/bin/env python3

"""Probando el argparse"""

from pprint import pprint as pp
import argparse

# abre = open('test_text.txt')

# ver = { line[0].upper(): line.rstrip() for line in abre }

# pp(ver)

dictA = { 'Uno': '1', 'Dos':'2', 'Tres':'3','Cuatro':'4'}

pp(dictA)

def argumentos():
    parse = argparse.ArgumentParser(
        description='Prueba de argumentos',
        formatter_class=argparser.ArgumentDefaultsHelpFormatter
    )

    parse.add_argument()