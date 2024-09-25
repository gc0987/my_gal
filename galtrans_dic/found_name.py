import os

path = './' + 'gt_input\\'
all_ = os.listdir(path)


class Buf:
    def __init__(self):
        self.he = [''] * 100000
        self.j = 0
        self.c = [''] * 100000


b = Buf()


def cl(hz, b):
    j = b.j
    he = b.he
    c = b.c
    l = ''
    for file in all_:
        f = open(path + file, 'r', encoding='UTF8')
        t = f.read()
        f.close()
        l = l + t
    al = l
    l = l.split(hz)
    for i in range(len(l)):
        words = l[i][-3:] + hz
        # if l[i][-1] == '"':
        #     continue
        # if l[i][-1] == ']':
        #     continue
        if words not in he:
            he[j] = words
            c[j] = len(al.split(words))
            j = j + 1
    b.j = j
    b.he = he
    b.c = c
    return b


def cl1(hz, b):
    j = b.j
    he = b.he
    c = b.c
    l = ''
    for file in all_:
        f = open(path + file, 'r', encoding='UTF8')
        t = f.read()
        f.close()
        l = l + t
    al = l
    l = l.split(hz)
    for i in range(len(l)):
        if i == len(l) - 1:
            break
        words = l[i][-2:] + hz + l[i + 1][0:2]
        if words not in he:
            he[j] = words
            c[j] = len(al.split(words))
            j = j + 1
    b.j = j
    b.he = he
    return b


atc1 = 'くん,ちゃん,さん,お嬢さん,先生,先輩,様'.split(',')
for a in atc1:
    b = cl(a, b)
atc2 = '○,〇,×'.split(',')
for a in atc2:
    b = cl1(a, b)
he = b.he[0:b.j]
b1 = Buf()
b1.j = b.j
max_ = 0
for i in range(b.j):
    js = int(b.c[i])
    if max_ < js:
        max_ = js
j = 0
while max_ != 0:
    if max_ not in b.c:
        max_ = max_ - 1
        continue
    for i in range(b.j):
        js = int(b.c[i])
        if js == max_:
            b1.he[j] = b.he[i]
            b1.c[j] = b.c[i]
            j = j + 1
    max_ = max_ - 1
w = b1.he[0:b.j]
c = b1.c[0:b.j]
hj = len(w) * ['']
for i in range(b.j):
    hj[i] = w[i] + '\t' + str(c[i])
f = open('项目GPT字典.txt', 'r', encoding='UTF8')
l = f.read().split('\n')
f.close()

for i in range(len(hj)):
    for j in range(len(l)):
        if l[j].split('\t')[0] in hj[i]:
            hj[i] = '[null]'
hj1 = len(hj) * ['']
k = 0
for i in range(len(hj)):
    if hj[i] == '[null]':
        continue
    hj1[k] = hj[i]
    k = k + 1
hj = hj1[0:k]
hj = '\n'.join(hj).replace('[null]', '')
f = open('name_plus.txt', 'w', encoding='UTF8')
f.write(hj)
f.close()
# 搜索  くん
# 搜索  ちゃん
# 搜索  さん
# 搜索  お嬢さん
# 搜索  先生
# 搜索  先輩
# 搜索  様
# 搜索  ○
# 搜索  〇
# 搜索  ×
