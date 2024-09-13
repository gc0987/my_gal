import os
path = os.path.dirname(os.path.realpath(__file__)) + '\\'
def getkey():
    a = open(path+'世界ノ全テ._key', 'r', encoding='UTF8').read().split('\n')
    a0 = bytes.fromhex(a[0])
    a1 = bytes.fromhex(a[1])
    a2 = len(a0) * ['']
    for i in range(len(a0)):
        a2[i] = a0[i] ^ a1[i]
    return a2
def _dec(bl,a2):
    pass
    if bl[0] == ' ':
        bl = bl[1:]
    if bl[-1] == ' ':
        bl = bl[:-1]
    c = bl.replace(' ',' ')
    c = bytes.fromhex(c)
    d = len(c) * ['']
    j = len(d)
    # print(bl)
    st = 0
    if j>len(a2):
        if len(a2)-j<=0:
            if '97 1F' in bl[0:6] or '97 2A'  in bl[0:6]:
                # print(bl[0:6])
                # print(len(a2)-j)
                # print(bl)

                pass
            else:
                # print(len(a2)-j)
                # print(bl)
                st = 1
    sy = ''
    di = 0
    for i in range(len(a2)):
        if i < j:
            d[i] = c[i] ^ a2[i]
            d[i] = hex(d[i]).replace('0x','')
            if len(d[i]) == 1:
                d[i] = '0' + d[i]
            di = di + 1
        else:
            # sy =''
            # d[i] = c[i]
            # print(a2[i])
            break
    d = ' '.join(d)
    _d = d
    d= bytes.fromhex(d)
    case = 0
    play = 0
    if case ==1:
        d = d.decode('cp932')
    else:
        c = d
        d = ''
        for i in range(0,len(c),2):
            if len(c[i:i+2]) == 1:return d, _d
            try:
                d = d +(c[i:i+2].decode('cp932')) + ''
                if i ==0:
                    if len(d) ==2:
                        play = 1
            except:
                # print('错误')
                # print(d)
                return d, _d
                d = d + '' +(c[i:i+2].decode('cp932'))
            if st:return '',_d
            if '\\w' in d:return d,_d
            if '"t' in d: return d, _d
            if '(' in d: return d, _d
            if '@A' in d:return d[0:2], _d
            if '^' in d:return '',_d

        if play:
            if len(d.encode('cp932'))!=len(d):
                return '', _d
            else:
                return '', _d
            #
    return d,_d
def _en(l1,l2,start):
    try:
        a1 = l1
    except:
        print(l1)
        print('dec_en._en()错误')
        exit(1)
    a1 = list(a1)
    a2 = l2
    j = 0
    for i in range(start,len(l2)):
        # print(i)
        # print(i,j,len(a1),len(l2))
        a1[j] = hex(a2[i] ^ a1[j]).replace('0x','')
        if len(a1[j])==1:
            a1[j] = '0' + a1[j]
        j = j + 1
        if j== len(a1):
            break
    # print(a1)
    try:
        a1 = ' '.join(a1)
    except:
        print(a1)
        print(start,len(l2),len(a1))
        exit()
    # a1 = ' '.join(a1)
    try:
        a2 = bytes.fromhex(a1)
    except:
        print(a1)
        exit()
    return a2
# bl = '97 1F F6 87 80 1A C2 87 21 E4 47 68 98 B9 8C 82 C4 0E A6 E8 B0 87 72 98 5F C6 EC 2B DE FA 4A E4 E3 EC 56 AD E0 4B 2C 88 8C 2B AE 50 F8 44 FA DF 28 24 14 C9 10 81 DE B8 AB CD 5E 6B 23 D7 AA C0 59 48 B6 F9 40 5A 82 C5 EC 75 0E 74 54 45 5A 30 8D CC 66 D6 70 A0 31 B0 0E 19 BE 4C 9A 97 0A 20 B4 37 16 C4 A0 BF F4 13 4C 66 63 12 B8 06 BA 1D EB 1C C6 34 D0 2F 92 64 7C FB 1E AC E8 9E 69 8B CA A8 24 22 00 00 03'
# p,p1 = _dec(bl,getkey())
# print(p1.upper())
# print(p)
# a1 = ''
# a2 = getkey()
# start = 0
# print(_en(a1,a2,start))
# for i in range(1,9):
#     print(i)

