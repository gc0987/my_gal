f = open('example.txt','r',encoding='utf8')
l = f.read().replace('>','>\n')
l = l.split('\n')
names = [''] * 10000
si = 0
for i in range(len(l)):
    if 'title="Female">'.upper()in l[i].upper():
        name = l[i-1].split('</small>')[0]
        if ' '  in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '小姐', '先生', '前辈']
            fullname = name.replace(' ','')
            temp = name
            name = temp.split(' ')
            fname = name[1]
            lname = name[0]
            names[si] = names[si] + lname + '' + '\t' + lname + 're' + '\t' + fullname + '’s lastname,girl' + '\n'
            names[si] = names[si] + fname + '' + '\t' + fname + 're' + '\t' + fullname + '’s firstname,girl' + '\n'
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + fname + jp[i1] + '\t' + fname +'re'+ chs[i1] + '\t' + 'girl' + '\n'
                names[si] = names[si] + lname + jp[i1] + '\t' + lname +'re'+ chs[i1] + '\t' + 'girl' + '\n'
        elif '　' in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '小姐', '先生', '前辈']
            fullname = name.replace('　', '')
            temp = name
            name = temp.split('　')
            fname = name[1]
            lname = name[0]
            names[si] = names[si] + lname + '' + '\t' + lname + 're' + '\t' + fullname + '’s lastname,girl' + '\n'
            names[si] = names[si] + fname + '' + '\t' + fname + 're' + '\t' + fullname + '’s firstname,girl' + '\n'
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + fname + jp[i1] + '\t' + fname +'re'+ chs[i1] + '\t' + 'girl' + '\n'
                names[si] = names[si] + lname + jp[i1] + '\t' + lname +'re'+ chs[i1] + '\t' + 'girl' + '\n'
        elif '・' in name:
            name1 = name.split('・')
            for name in name1:
                num = [1, 2, 3, 4, 5]
                jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
                chs = ['君', '酱', '小姐', '先生', '前辈']
                for i1 in range(len(num)):  # 1 2 3
                    names[si] = names[si] + name + jp[i1] + '\t' + name+'re' + chs[i1] + '\t' + 'girl' + '\n'
                names[si] = names[si] + name + '' + '\t' + name + 're' + '\t' + 'girl' + '\n'
        elif ' ' not in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '小姐', '先生', '前辈']
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + name + jp[i1] + '\t' + name +'re'+ chs[i1] + '\t' + 'girl' + '\n'
            names[si] = names[si] + name + '' + '\t' + name + 're' + '\t' + 'girl' + '\n'
        si = si + 1
    elif 'title="male">'.upper()in l[i].upper():
        name = l[i-1].split('</small>')[0]
        if ' '  in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '桑', '先生', '前辈']
            fullname = name.replace(' ','')
            temp = name
            name = temp.split(' ')
            fname = name[1]
            lname = name[0]
            names[si] = names[si] + lname + '' + '\t' + lname + 're' + '\t' + fullname + '’s lastname,boy' + '\n'
            names[si] = names[si] + fname + '' + '\t' + fname + 're' + '\t' + fullname + '’s firstname,boy' + '\n'
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + fname + jp[i1] + '\t' + fname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
                names[si] = names[si] + lname + jp[i1] + '\t' + lname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
        elif '　' in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '桑', '先生', '前辈']
            fullname = name.replace('　', '')
            temp = name
            name = temp.split('　')
            fname = name[1]
            lname = name[0]
            names[si] = names[si] + lname + '' + '\t' + lname + 're' + '\t' + fullname + '’s lastname,boy' + '\n'
            names[si] = names[si] + fname + '' + '\t' + fname + 're' + '\t' + fullname + '’s firstname,boy' + '\n'
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + fname + jp[i1] + '\t' + fname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
                names[si] = names[si] + lname + jp[i1] + '\t' + lname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
        elif '・' in name:
            name1 = name.split('・')
            for name in name1:
                num = [1, 2, 3, 4, 5]
                jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
                chs = ['君', '酱', '桑', '先生', '前辈']
                for i1 in range(len(num)):  # 1 2 3
                    names[si] = names[si] + name + jp[i1] + '\t' + name+'re' + chs[i1] + '\t' + 'boy' + '\n'
                names[si] = names[si] + name + '' + '\t' + name + 're' + '\t' + 'boy' + '\n'
        elif ' ' not in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '桑', '先生', '前辈']
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + name + jp[i1] + '\t' + name +'re'+ chs[i1] + '\t' + 'boy' + '\n'
            names[si] = names[si] + name + '' + '\t' + name + 're' + '\t' + 'boy' + '\n'
        si = si + 1
    elif 'Fema--le'.upper()in l[i].upper():
        name = l[i-1].split('</small>')[0]
        if ' '  in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '桑', '先生', '前辈']
            fullname = name.replace(' ','')
            temp = name
            name = temp.split(' ')
            fname = name[1]
            lname = name[0]
            names[si] = names[si] + lname + '' + '\t' + lname + 're' + '\t' + fullname + '’s lastname,boy' + '\n'
            names[si] = names[si] + fname + '' + '\t' + fname + 're' + '\t' + fullname + '’s firstname,boy' + '\n'
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + fname + jp[i1] + '\t' + fname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
                names[si] = names[si] + lname + jp[i1] + '\t' + lname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
        elif '　' in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '桑', '先生', '前辈']
            fullname = name.replace('　', '')
            temp = name
            name = temp.split('　')
            fname = name[1]
            lname = name[0]
            names[si] = names[si] + lname + '' + '\t' + lname + 're' + '\t' + fullname + '’s lastname,boy' + '\n'
            names[si] = names[si] + fname + '' + '\t' + fname + 're' + '\t' + fullname + '’s firstname,boy' + '\n'
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + fname + jp[i1] + '\t' + fname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
                names[si] = names[si] + lname + jp[i1] + '\t' + lname +'re'+ chs[i1] + '\t' + 'boy' + '\n'
        elif '・' in name:
            name1 = name.split('・')
            for name in name1:
                num = [1, 2, 3, 4, 5]
                jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
                chs = ['君', '酱', '桑', '先生', '前辈']
                for i1 in range(len(num)):  # 1 2 3
                    names[si] = names[si] + name + jp[i1] + '\t' + name+'re' + chs[i1] + '\t' + 'boy' + '\n'
                names[si] = names[si] + name + '' + '\t' + name + 're' + '\t' + 'boy' + '\n'
        elif ' ' not in name:
            num = [1, 2, 3, 4, 5]
            jp = ['くん', 'ちゃん', 'さん', '先生', '先輩']
            chs = ['君', '酱', '桑', '先生', '前辈']
            for i1 in range(len(num)):  # 1 2 3
                names[si] = names[si] + name + jp[i1] + '\t' + name +'re'+ chs[i1] + '\t' + 'boy' + '\n'
            names[si] = names[si] + name + '' + '\t' + name + 're' + '\t' + 'boy' + '\n'
        si = si + 1
names = '\n'.join(names[0:si]).replace('\n\n','\n')
names = names.split('\n')
f = open('字典.txt','r',encoding='utf8')
ld = f.read().split('\n')
f.close()
tr = len(names) * ['']
# print(names)
for i in range(len(tr)):
    if names[i]=='':
        continue
    tr[i] = names[i].split('\t')[1]
    if len(tr[i].replace('re',''))==2:
        if '酱'==tr[i].replace('re','')[-1]:
            tr[i] ='小'+ tr[i][0]
            # print(tr[i])
tr = '\\'.join(tr)
for i in ld:
    a = i.split(',')[1]
    b = i.split(',')[0]
    tr = tr.replace(a,b)
tr = tr.split('\\')
for i in range(len(tr)):
    if names[i]=='':
        continue
    names1 = names[i].split('\t')
    names1[1] = tr[i]
    names[i] = '\t'.join(names1)
names = '\n'.join(names)
fw = open('项目GPT字典.txt','w',encoding='UTF-8')
fw.write(names)
fw.close()