#!/usr/bin/env python3
"""
LanguageLearner - Entry point script

This script serves as a simple entry point to run the Language Learning application.
Run this script from the root directory of the project.
"""

import os
import sys
import cv2

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the main module (don't execute it yet)
from src import main

if __name__ == "__main__":
    print("Starting LanguageLearner...")
    print("Press Ctrl+C to exit.")
    
    try:
        # Run the main application
        if hasattr(main, '__name__') and main.__name__ == '__main__':
            pass  # Already running from main
        else:
            # Call the main application code
            main.main()
            
    except KeyboardInterrupt:
        print("\nExiting LanguageLearner...")
        cv2.destroyAllWindows()
        main.engine.stop()
        sys.exit(0) 