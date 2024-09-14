import os
p = './transl_cache\\'
files = os.listdir(p)
f = open('合.txt','r',encoding='UTF8')
l = f.read().split('\n666666\n')
f.close()
i = 0
for file in files:
    fw = open(p+file,'w',encoding='UTF8')
    fw.write(l[i])
    i = i + 1
    fw.close()
