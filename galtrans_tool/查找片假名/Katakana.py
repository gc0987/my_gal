def getkat():
    f = open('原文.txt', 'r', encoding='UTF16')
    c = f.read()
    f.close()
    Katakana = '''
ァィゥヴェォカヵキクケコ
サシスセソタチツッテトヰン
ナニヌネノハヒフヘホヱ
マミムメモャュョヮヲ
アイウエオガギグゲゴ
ザジズゼゾダヂヅデド
パピプペポバビブベボ
ラリルレロヤユヨワ
'''.replace('\n', '')
    kats = 10000 * ['']
    j = 0
    words = ''
    for word in c:
        if word in Katakana:
            words = words + word
        else:
            if words != '' and len(words)!=1:
                if words not in kats:
                    kats[j] = words
                    j = j + 1
                    # print(words)
            words = ''

    return kats[0:j]
k = getkat()
f = open('片假名.txt','w',encoding='UTF8')
f.write('\n'.join(k))
f.close()
