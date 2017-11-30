# -*- coding: utf-8 -*-

from gdsCAD import *

# Create some things to draw
text = shapes.Label('Hello\nPoyo-Poyo', 200, (0, 0))

# Create cell
cell = core.Cell('EXAMPLE')
cell.add(text)

# Add the cell to a Layout and save
layout = core.Layout('LIBRARY')
layout.add(cell)
layout.save('poyo.gds')
