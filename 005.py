import re
f = open("test051.txt", "r", encoding="utf-8")
lis = [x.rstrip() for x in f.readlines()]
f.close()
print('Исходный текст:')
print(lis)
print('')
for x in lis:
    txt = re.sub('[0-9]+', lambda x: str(3*int(x.group(0))+5), x)
    print(txt)