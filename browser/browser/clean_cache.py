import os
import sys

# Ruta al script actual
script = sys.argv[0]

# Ejecutar nuevamente el script actual
os.execv(script, sys.argv)
