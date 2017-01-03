import sys
from cx_Freeze import setup, Executable

setup(
    name = "BMI",
    version = "0.1",
    description = "BMI.",
    executables = [Executable("main2.py", base = "Win32GUI")])