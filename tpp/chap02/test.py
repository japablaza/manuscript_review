#!/usr/bin/env python3
"""Prueba del archivo nidodecuervo.py"""

import os
from subprocess import getstatusoutput, getoutput

archivo = './nidodecuervo.py'

consonantes = ['brigatine', 'clipper', 'dreadnought', 'frogate', 'galleon',
               'haddock', 'junk', 'ketch', 'longbopat', 'mullet', 'narwhal',
               'porpoise', 'quay', 'regatta', 'submarine', 'tanker', 'vessel',
               'whale', 'xebec', 'yatch', 'zebrafish']

vocales = ['aviso', 'eel', 'iceberg', 'octupus', 'upbound']

oracion = 'Ahoy, Capitan, {} {} off the larboard bow!'


def test_existe():
    """El archivo existe?"""
    assert os.path.isfile(archivo)


def test_ayuda():
    """Se puede usar ayuda?"""
    for bandera in ['-h', '--help']:
        rv, comand = getstatusoutput(f'{archivo} {bandera}')
        assert rv == 0
        assert comand.lower().startswith('usage')


def test_consonante():
    """clipper --> a clipper"""
    for palabra in consonantes:
        comand = getoutput(f'{archivo} {palabra}')
        assert comand.strip() == oracion.format('a', palabra)


def test_consonante_upper():
    """clipper --> a Clipper"""
    for palabra in consonantes:
        comand = getoutput(f'{archivo} {palabra.title()}')
        assert comand.strip() == oracion.format('a', palabra.title())


def test_vocal():
    """eel --> an eel"""
    for vocal in vocales:
        comand = getoutput(f'{archivo} {vocal}')
        assert comand.strip() == oracion.format('an', vocal)


def test_vocal_upper():
    """eel --> an Eel"""
    for vocal in vocales:
        comand = getoutput(f'{archivo} {vocal.title()}')
        assert comand.strip() == oracion.format('an', vocal.title())
