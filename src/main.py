from misskey import Misskey
from pyenv import *

mi = Misskey('misskey.io')
mi.token = TOKEN2

mi.notes_create('hello misskey!')

# docs: https://misskeypy.readthedocs.io/ja/latest/
