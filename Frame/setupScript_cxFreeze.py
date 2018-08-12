import sys, os
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = "C:/Users/quan_/AppData/Local/Programs/Python/Python36"
base = None
if sys.platform == "win32":
    base = "Win32GUI"
else:
    print("sys not define")
executable = Executable('separatePeakWx.py', base=base)

includefiles = ['../src/dividData.py', '../src/doIt.py', '../src/fileIO.py', '../src/TemplateWx.py']
exclude = ['tkinter']
packages = ['math', 'numpy']
setup(
    name = "SeparatePeak",
    version = "1.0",
    options = {'build_exe':{'packages':packages, 'excludes':exclude, 'include_files':includefiles}},
    executables = [executable]
    )