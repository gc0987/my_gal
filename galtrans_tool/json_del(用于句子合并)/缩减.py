f = open('原文old.txt','r',encoding='UTF8')
lo = f.read().split('\n')
f.close()
f = open('原文new.txt','r',encoding='UTF8')
ln = f.read().split('\n')
f.close()
f = open('合.txt','r',encoding='UTF8')
lh = f.read().split('{')
f.close()
ln1 = len(ln) * ['']
k = 0
for i in range(len(ln)):
    if ln[i] not in lo:
        ln1[i] = '[n]'
        continue
    for j in range(k,len(lo)):
        # print(j)
        if lo[j] =='':
            continue
        if ln[i] == lo[j]:
            ln1[i] = '  {'+lh[j+1].split('}')[0] + '}'
            lo[j] = ''
            k = j

            break
maxlen = 3000
for i in range(len(ln1)):
    if ln1[i]!='[n]':
        # print(ln1[i])
        # exit(1)
        l = ln1[i].split('\n')
        if i == len(ln1) - 1:
            if ']' not in ln1[i]:
                ln1[i] = ln1[i] + ']'
        try:
            l[1] = '    "index": ' + str((i+0)%maxlen + 1) + ','
        except:
            print(ln1[i])
            print(i)
            continue
        ln1[i] = '\n'.join(l)
        if (i + 0) % maxlen + 1 == maxlen:
            ln1[i] = ln1[i] + '\n]'
        if (i + 0) % maxlen + 1 == 1:
            ln1[i] = '[\n'+ln1[i]
            # print()
    else:
        if (i + 0) % maxlen + 1 == maxlen:
            ln1[i] = ln1[i] + '\n]'
        if (i + 0) % maxlen + 1 == 1:
            ln1[i] = '[\n' + ln1[i]
            # print()
ln1 = ',\n'.join(ln1)
ln1 = ln1.replace('[n],','').replace('],',']\n666666')
ln1 = ln1.replace(',\n]','\n]')
f = open('合new.txt','w',encoding='UTF8')
f.write(ln1)
f.close()