def aaa(Original ,trans):
    if '@r' in Original:
        spf = '@{'
        spf1 = '@}'
        if spf in Original:
            print(Original)
            le1 = Original.split(spf)
            Original = ''
            for kh in le1:
                if spf1 in kh:
                    Original = Original.replace('@r', '') + '' + kh.split(spf1)[1]
                else:
                    Original = Original + kh.replace('@r', '')
            Original = Original
    if '\\n' in Original  or '@' in Original  or 'ω' in Original  or '･' in Original :
        Original  = Original 
        nameflag = ''
        maxl = 26
        stag = ['主人公---', '@p1', '@p2', '@p3', '@s', '@f', '@-', '@p', '@k', '@l', '@d', '@m', 'ω--', '\\----n',
                '･'] + [''] * 10
        rptag = list('ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅒㅔㅖㅘㅙㅚㅝㅞㅟㅢㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉ')
        ltg = Original .replace('　「', '「')
        if '@<' in Original :
            ltg1 = ltg.split('@<')
            gi = 0
            stop = 0
            for tg in range(len(stag)):
                if stag[tg] == '':
                    for gj in range(len(ltg1)):
                        if '@>' in ltg1[gj]:
                            stag[tg] = '@<' + ltg1[gj].split('@>')[0] + '@>'
                            ltg1[gj] = ''
                            tg = tg + 1
                            continue
                        taggalg = ''.join(ltg1[gj])
                        if '@>' not in taggalg:
                            stop = 1
                            continue
                else:
                    pass
                if stop:
                    break
            # print(stag)
        for tg in range(len(stag)):
            if stag[tg] == '':
                break
            ltg = ltg.replace(stag[tg], rptag[tg])
        le1 = list(ltg)
        le2 = list(trans)
        max1 = len(le2)
        case = 1
        if case == 1:
            for e in range(len(le1)):
                try:
                    for tg in range(len(stag)):
                        if stag[tg] == '':
                            break
                        if le1[e] == rptag[tg]:
                            le2[e] = stag[tg] + le2[e]
                            # print(le1[e])
                            break
                except:
                    for tg in range(len(stag)):
                        if stag[tg] == '':
                            break
                        if le1[e] == rptag[tg]:
                            stag[tg]
                            le2[len(le2) - 1] = le2[len(le2) - 1] + stag[tg] + '　'
                            break
        else:
            for e in range(len(le2)):
                if e == 0:
                    continue
                if e % maxl == 0:
                    if ']' in nameflag:
                        le2[e] = '\\r\\n　' + le2[e] + ''
                    else:
                        le2[e] = '\\r\\n' + le2[e] + ''

        trans = ''.join(le2)
    return trans
if True:
    o = '万里音「お姉ちゃんにとっては重要なことなの！　@<=base+t1_203_b1@>ま、でも今は許してあげる。……それで？　サキちゃんはどう思うの？」'
    t = '万里音「对姐姐来说这很重要哦！不过现在就原谅你吧。……那么？小崎你怎么看？」'
    print(o)
    print(aaa(o,t))
    print()

    o = '千恵「@<\'$3pico@>くしゅん……っ」'
    t = '千恵「啾——」'
    print(o)
    print(aaa(o,t))
    print()

    o = '勇美「ほら、いつまでもベタベタしないのっ。崎人も早く、@<\'$1pico@>@<\'$2pico@>万里音さんから離れる！」'
    t = '勇美「喂，别一直黏在一起了。崎人，也快点离开万里音小姐吧！」'
    print(o)
    print(aaa(o,t))
    print()

    o = '@fドピュ、@fドピュッ、@fドピュピュ！'
    t = '喷射，喷射，喷射！'
    print(o)
    print(aaa(o,t))
    print()
