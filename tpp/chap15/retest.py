#!/usr/bin/env python3
'''This is a test for re'''

import re

text = 'Padre, padre, donde vas?'

test_list = text.split()

print(test_list)

test_re = re.split('(\W+)', text)

print(test_re)