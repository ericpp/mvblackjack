from distutils.core import setup
import py2exe
import glob

# import sys
# from cx_Freeze import setup, Executable
# setup(  name = "blackjack",
#         version = "0.1",
#         description = "Blackjack",
#         executables = [Executable("blackjack.py")])

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "blackjack.py"}],
    data_files = [('images', glob.glob('images/*'))],
    zipfile = None,
)
# setup(console=['blackjack.py'])