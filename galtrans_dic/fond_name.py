import os
def 队列(element,str_short):
    buffer = str_short
    for i in range(0, len(buffer) - 1):
        buffer[i] = buffer[i + 1]
    buffer[len(buffer) - 1] = element
    return str_short

日文json路径 = './' + 'gt_input\\'
if not os.path.exists(日文json路径):
    os.mkdir(日文json路径)
所有文件 = os.listdir(日文json路径)
后缀集合 = [''] * 100000
后缀集合1 = [''] * 100000


##搜索  くん
hz = 0
buf = [''] * 2
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == 'くん':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1

##搜索  ちゃん
buf = [''] * 3
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == 'ちゃん':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1
##搜索  ちゃん
buf = [''] * 3
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == 'ちゃん':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1

##搜索  さん
buf = [''] * 2
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == 'さん':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1
##搜索  お嬢さん
buf = [''] * 4
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == 'お嬢さん':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1

##搜索  先生
buf = [''] * 2
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == '先生':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1
##搜索  先輩
buf = [''] * 2
向前显示 = 4
向后显示 = 1 + 0    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == '先輩':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1
##搜索  ○
buf = [''] * 1
向前显示 = 2
向后显示 = 1 + 2    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == '○':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1

##搜索  〇
buf = [''] * 1
向前显示 = 2
向后显示 = 1 + 2    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == '〇':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1

##搜索  ×
buf = [''] * 1
向前显示 = 2
向后显示 = 1 + 2    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == '×':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1
##搜索  様
buf = [''] * 1
向前显示 = 2
向后显示 = 1 + 2    #向后必须大于等于1
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    for i in range(len(l)):
        单字 = l[i]
        buf = 队列(单字,buf)
        if ''.join(buf) == '様':
            词= ''.join(l[i-向前显示:i+向后显示])
            if 词 not in 后缀集合:
                后缀集合[hz] = 词
                后缀集合1[hz] = 词 + '\t' + 词
                hz = hz + 1
l1 = ''
for file in 所有文件:
    f = open(日文json路径 + file,'r',encoding='UTF8')
    l = f.read()
    f.close()
    l1 = l1 + l
for i in range(len(后缀集合[0:hz])):
    后缀集合[i] = 后缀集合[i] + '\t' + str(len(l1.split(后缀集合[i])))
f = open('项目GPT字典.txt','r',encoding='UTF8')
l = f.read().split('\n')
f.close()
hj = 后缀集合[0:hz]
for i in range(len(hj)):
    for j in range(len(l)):
        if l[j].split('\t')[0] in hj[i]:
            hj[i] = ''
    pass
hj = '\n'.join(hj)
后缀 = open('后缀.txt','w',encoding='UTF8')
后缀.write(hj)
后缀.close()

后缀1 = open('后缀1.txt','w',encoding='UTF8')
后缀1.write('\n'.join(后缀集合1))
后缀1.close()