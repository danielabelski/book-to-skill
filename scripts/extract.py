#!/usr/bin/env python3
"""
Extract text from a document file for book-to-skill processing.
Modular entrypoint wrapper.
"""

import os
import sys

# Ensure the parent directory of this script's directory (i.e. the repository root) 
# is in sys.path so that the modular 'extractor' package can be imported reliably.
sys.path.insert(0, str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from extractor.utils import main

if __name__ == "__main__":
    main()
