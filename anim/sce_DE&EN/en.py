import struct
import os

p1 = './原加密文件\\'
p2 = './原解密文件\\'
p3 = './翻译好的文件\\'
p4 = './翻译好的文件加密\\'
files1 = os.listdir(p1)
files2 = os.listdir(p2)
files3 = os.listdir(p3)
files4 = os.listdir(p4)
if not files3:
    exit()
for file in files1:
    f = open(p1 + file, 'rb')
    b1 = f.read()
    f.close()
    f = open(p2 + file, 'rb')
    b2 = f.read()
    f.close()
    f = open(p3 + file, 'rb')
    b0 = f.read()
    f.close()
    fw = open(p4 + file, 'wb')
    for i in range(len(b0)):
        xor = b1[i] ^ b2[i]
        bt = struct.pack('B', b0[i] ^ xor)
        fw.write(bt)
    fw.close()
    f.close()
