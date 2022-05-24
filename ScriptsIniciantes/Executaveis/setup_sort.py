from cx_Freeze import setup, Executable

setup(
    name="Sorteio R6",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("sorteio.py")])