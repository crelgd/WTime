import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["PyQt5"],
    "include_files": ["ui/", "Core/"]  # Добавьте папки с вашими UI-файлами и кодом Core
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="WTime",
    version="0.1",
    description="WTime application",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.pyw", base=base)]
)
