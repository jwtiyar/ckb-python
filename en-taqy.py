import arabic_reshaper
from bidi.algorithm import get_display
import re
import unicodedata

f = open('ckb.txt', 'r',encoding='utf-8')
d = open('ennew.txt', 'w',encoding='utf-8')
g = f.readlines()
for line in g:
    if line.startswith('\u0686') :
        d.write(line)
    print(line)

 
   


