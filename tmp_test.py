from konlpy.tag import Okt
import collections
import networkx as nx
from wordcloud import WordCloud
import matplotlib.pyplot as plt

okt = Okt()
f = open('output_tmp.txt', 'r', encoding='utf8')
cnt = 0
stop_words = ['생각','그냥','계속','정말','지금','다시','처음','저희', '혹시', '오늘',
              '확인', '가능성', '추천', '자꾸', '전혀', '그때', '바로', '부분', '이후',
              '거의','건가','보통', '냉이', '저번', '안해', '살짝', '조금', '가요',
              '시작', '질문', '답변', '다음', '때문', '어제', '중간', '원래', '경우','물이','뭔가','만약','정도']
not_stop_words = ['집', '술', '약', '방']
pair_counter = collections.Counter()
while True:
    sentence = f.readline()
    if not sentence:
        break
    l = okt.nouns(sentence)
    l = [i for i in l if (i not in stop_words and len(i) > 1) or i in not_stop_words]
    l = [(i, j) for i in l for j in l]
    for i, j in l:
        if i != j:
            pair_counter[i, j]+=1
    print('cnt: ', cnt)
    cnt += 1
tmp_counter = collections.Counter()
tmp_set = set()
for i, j in pair_counter:
    if (j, i) in tmp_set:
        tmp_counter[i, j] = pair_counter[i, j]
    else:
        tmp_set.add((i, j))
pair_counter = pair_counter & tmp_counter
print(pair_counter.most_common(100))