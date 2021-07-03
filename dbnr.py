import quo
import os
import sys
from src.debonair.core import *

if __name__ == "__main__":
  try:
    main.core()
  except KeyboardInterrupt:
    os.system("clear")
    quo.flair(f"Exitting...", foreground="vred")
    logo.exit()
