import os
import sys

# Make `import bot` work when pytest runs from any directory.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
