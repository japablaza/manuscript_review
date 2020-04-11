#!/usr/bin/env python3
"""This is a list of dict test"""

from pprint import pprint

csvfile = '/home/pepe/bin/manuscript_review/tpp/chap19/exercises.csv'

with open(csvfile) as fl:
    cabecera = fl.readline().rstrip().split(',')
    guardar = []
    for linea in fl:
        guarda = dict(zip(cabecera, linea.rstrip().split(',')))
        guardar.append(guarda)
    # pprint(guardar)

fl = open(csvfile)
print(fl.readline())