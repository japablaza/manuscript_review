#!/usr/bin/env python3
"""Probando el codigo en hola.py."""

import os
from subprocess import getstatusoutput, getoutput

archivo = './hola.py'


def test_existe():
    """Existe el archivo?"""
    assert os.path.isfile(archivo)


def test_corre():
    """Puedes correr el archivo"""
    comand = getoutput(f'python3 {archivo}')
    assert comand.strip() == 'Hola, Mundo!'


def test_ejecuta():
    """Se ejecuta el codigo con la salida 'Hola, Mundo!'. Usa chmod u+x"""
    comand = getoutput({archivo})
    assert comand.strip() == 'Hola, Mundo!'


def test_usar():
    """Se puede usar el codigo"""
    for bandera in ['-h', '--help']:
        rv, comand = getstatusoutput(f'{archivo} {bandera}')
        assert rv == 0
        assert comand.lower().startswith('usage')


def test_input():
    """Prueba del codifo"""
    for palabra in ['Pepe', 'Pato']:
        for opcion in ['-n', '--name']:
            rv, comand = getstatusoutput(f'{archivo} {opcion} {palabra}')
            assert rv == 0
            assert comand.strip() == f'Hola, {palabra}!'
