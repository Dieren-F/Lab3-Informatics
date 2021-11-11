import re

def f(match):
    return str(3*int(match)+5)

f = open("test051.txt", "r", encoding="utf-8")
lis = [x.rstrip() for x in f.readlines()]
f.close()
def replacer(m):
    digitals = []
    for x in m.groups():
        if x in ['+', '-', '*', '/', '=']:
            if x=='=':
                print('=')
        else:
            digitals.append(int(x))
            print(digitals)
    return 's'

for x in lis:
    txt = re.sub(r'(\d+)\s*([\+\-\\/])\s(\d+)\s*(=)\s*(\d+)', replacer, x)
    print(txt)