import os
f = open('合.txt','r',encoding='utf8')
l = f.read()
f.close()
l = l.replace('\n]\n666666\n[\n',',\n').replace('[\n','').replace('\n]','')
l = l.replace('\n666666\n','')
l = l.split('},')
# f = open('合new.txt','w',encoding='utf8')
# f.write(l)
# f.close()
f = open('原文.txt','r',encoding='utf8')
l1 = f.read().split('\n')
f.close()
f = open('原文new.txt','r',encoding='utf8')
l2 = f.read().split('\n')
f.close()
l3 = len(l2) * ['']
j = 0
for i in range(len(l2)):
    if '6666' in l2[i]:
        # print(l2[i])
        l3[i] = '\n  {\n[null]\n  '
    else:
        try:
            l3[i] = l[j]
        except:
            print(j)
            print(i)
            print('错误')
            exit(1)
        j = j + 1
for i in range(len(l3)):
    index = i%3000+1
    # print(index)
    if 'index' in l3[i]:
        li = l3[i].split('\n')
        for j in range(len(li)):
            if 'index' in li[j]:
                li[j] = '    "index": ' + str(index) + ','
        l3[i] = '\n'.join(li)
l3 = '},'.join(l3)
l3 = l3.split('},')
p = './transl_cache\\'
p1 = './new_transl_cache\\'
files = os.listdir(p)
j = 0
try:
    os.mkdir(p1)
except:
    pass
for i in range(0,len(l3),3000):
    file = files[j]
    f = open(p1 + file, 'w', encoding='utf8')
    inc = '},'.join(l3[i:i+3000])
    if '[null]' in inc:
        inc = inc.split('},')
        for k in range(len(inc)):
            if '[null]' in inc[k]:
                continue
            else:
                ind = inc[k].split('\n')
                for kk in range(len(ind)):
                    if 'post_zh_preview' in ind[kk]:
                        ind[kk] = '[n]'
                        ind [kk-1] = ind [kk-1][0:-1]
                inc[k] = '\n'.join(ind).replace('\n[n]\n','\n')
        inc = ('},').join(inc).replace('  {\n[null]\n  },','').replace('\n\n','')
        inc = inc.replace(',\n  },','\n  }')
    f.write('[\n')
    f.write(inc)
    if j!=len(files)-1:
        f.write('\n  }\n]')
    else:
        f.write('\n]')
    f.close()
    j = j + 1
l3 = '},'.join(l3)
f = open('合new.txt','w',encoding='utf8')
f.write(l3)
f.close()