import re
f = open("test011.txt", "r")
lis = [x for x in f.readlines()]
f.close()
pattern = '=<{/'
print(re.findall(pattern, ''.join(lis)))
print('Количество смайликов:')
print(len(re.findall(pattern, ''.join(lis))), 'штук')