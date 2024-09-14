import os
p = './transl_cache\\'
files = os.listdir(p)
fw = open('合.txt','wb')
for file in files:
    f = open(p+file,'rb')
    fw.write(f.read())
    fw.write(b'\n666666\n')
    f.close()
fw.close()