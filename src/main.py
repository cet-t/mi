from misskey import Misskey
from pyenv import *

INSTANCE_NAME = 'misskey.io'

mi = Misskey(INSTANCE_NAME)
mi.token = TOKEN2

# mi.notes_create('hello misskey!')
# print(mi.meta()['name'])

# docs: https://misskeypy.readthedocs.io/ja/latest/
