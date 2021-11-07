import re
f = open("test035.txt", "r", encoding="utf-8")
lis = [x.rstrip() for x in f.readlines()]
f.close()
for x in lis:
    m = re.search(r'([А-ЯA-Z])[а-яa-z]+\s\1\.\1\.\ P000$', x)
    if m is None:
        print(x)