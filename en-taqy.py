import arabic_reshaper
from bidi.algorithm import get_display
import unicodedata

""" f = open('ckb.txt', 'r',encoding='utf-8')
d = open('ennew.txt', 'w',encoding='utf-8')
g = f.readlines()
for line in g:
    if line.startswith('\u0686') :
        d.write(line)
    print(line)
 """
""" 
with open("ckb.txt", 'r+', encoding='utf-8') as f:
    lines = f.readlines()

with open("ckb.txt", 'w+', encoding='utf-8') as f:
    lines = list(filter(lambda lines: len(lines) <= 4, lines))
    f.writelines(lines) 

print(len(lines))
 """

""" lines = [line for line in open("ckb.txt", 'r+', encoding='utf-8').readlines() if len(line) < 4]
with open("ckb.txt", 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines)) """

f = open('ckb.txt', 'r',encoding='utf-8')
d = open('ennew.txt', 'w',encoding='utf-8')
g = f.readlines()
for line in g:
    if len(line) < 4:
        d.writelines(line)
    else:
        pass