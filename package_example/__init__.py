# package_example/__init__.py
# package_example/__init__.py
import sys
import os

# Go one directory up to include big_project in Python’s search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ttt import no

__version__ = "0.1.0"
