
import sys
from pony.util import builder

NAMES = [
    'SSE',
    'COW',
]

builder(sys.modules[__name__])
