import sys
from cx_Freeze import setup, Executable

# 依赖项
build_exe_options = {
    "excludes": ["tkinter", 'email', 'collection', 'libcrypto', "xml", "logging", "distutils", "pydoc_data", "unittest", "test", "pydoc", "tkinter", "unittest", "email", "html"],
    "packages": ["os", "sys", "glob", "urllib.request", "json", "gzip", "subprocess"],
    "zip_include_packages": ["collections", "encodings", "importlib"],
    "zip_exclude_packages": [],
    "include_files": [],
    "include_msvcr": False,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="your_app_name",
    version="0.1",
    description="My Python Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("pr-downloader.py")],
)
