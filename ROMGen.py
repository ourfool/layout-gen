# -*- coding: utf-8 -*-

"""Summary

Attributes:
    grid (TYPE): val for Cell
    layout (TYPE): val for layout
    temp (int): temp
"""

import numpy as np
from gdsCAD import *


def xbar(w1, w2):
    """Summary

    Args:
        w1 (TYPE): Description
        w2 (TYPE): Description
    Returns:
        TYPE: Description
    """
    cell = core.Cell('XBAR')
    xstrip = shapes.Rectangle((0, 0), (32, w1))
    ystrip = shapes.Rectangle((0, 0), (w2, 128), layer=2)

    for i in range(32):
        d = (0, i * w1 * 2)
        cell.add(utils.translate(xstrip, d))

    for i in range(8):
        d = (i * w2 * 2, 0)
        cell.add(utils.translate(ystrip, d))

    return cell


def via(w1, w2):
    """Summary

    Args:
        w1 (TYPE): Description
        w2 (TYPE): Description
    Returns:
        TYPE: Description
    """
    cell = core.Cell('VIA')
    square = shapes.Rectangle((0.5, 0.5), (1.5, 1.5), layer=3)
    d = (w1, w2)
    cell.add(utils.translate(square, d))

    return cell


grid = core.Cell('GRID')
grid.add(xbar(2, 2))

temp = 0
with open('rom.bin', 'r', encoding='utf-8') as f:
    for line in f:
        items = line
        print(items)
        for n in range(8):
            if (items[n] == '1'):
                print('one')
                grid.add(via(n * 4, temp * 4))

        temp += 1


# Add the copied cell to a Layout and save
layout = core.Layout('LIBRARY')
layout.add(grid)
layout.save('rom.gds')
