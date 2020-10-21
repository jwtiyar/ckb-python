import arabic_reshaper
from bidi.algorithm import get_display
import unicodedata
from sys import argv
import string


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
 
def labrdny_wshey_drezh():
    script, perrge1, perrge2 = argv

    print("Scripteket brytye le", script)

    f = open(perrge1, 'r',encoding='utf-8')
    d = open(perrge2, 'w',encoding='utf-8')

    g = f.readlines()

    for line in g:
        if len(line) < 4:
            d.writelines(line)
        else:
            pass

def labrdny_Xallbendy():
    with open('ckb.txt', "r+", encoding="utf-8") as t:

        s = t.read()
        encam = s.translate(str.maketrans("","", string.punctuation))

    with open('ennwe.txt', 'w+', encoding='utf-8') as perrey2:
        perrey2.write(encam)
        print(perrey2)

labrdny_wshey_drezh()
labrdny_Xallbendy()
     
# Python 3.9 changelog check.
a = {10,12}
b = {5, 15}

c = a | b

print(c)
