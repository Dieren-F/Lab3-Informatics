import re
f = open("test021.txt", "r", encoding="utf-8")
txt = ' '.join([x.rstrip() for x in f.readlines()])
print('Исходный текст:')
print(txt)
f.close()
print('')
txt = re.sub(r'\b(\w+)\b\s+\b\1\b', r'\1', txt)
print(txt)