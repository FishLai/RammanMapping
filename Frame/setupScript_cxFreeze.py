import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
else:
    print("sys not define")
executable = Executable('separatePeakWx.py', base=base)
setup(
    name = "SeparatePeak",
    version = "1.0",
    executables = [executable]
    )