#!/usr/bin/env python3

jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
          '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

numtex = 'ABC123'

# for x in numtex:
#     print(x, x in jumper)

# for x in numtex:
#     print(x, jumper[x] if x in jumper else x)

for x in numtex:
    print(jumper.get(x, x), end="")
