from konlpy.tag import Okt
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt

okt = Okt()
f = open('output_asdf.txt', 'r', encoding='utf8')
cnt = 0
stop_words = ['있다', '없다', '그렇다', '같다', '아니다', '좋다', '이다', '어떻다', '안되다', '이렇다', '스럽다', '안녕하다', '부탁드리다', '괜찮다', '많다', '좋아하다', '정확하다', '자세하다', '궁금하다']
adj_counter = collections.Counter()
while True:
    sentence = f.readline()
    if not sentence:
        break
    l = okt.pos(sentence, norm=True, stem=True)
    for i in l:
        if i[1] == 'Adjective' and i[0] not in stop_words:
            adj_counter[i[0]] += 1
    print('cnt: ', cnt)
    cnt += 1
print(adj_counter)
wordcloud = WordCloud(
    font_path = './NanumBarunGothic.ttf',
    width = 800,
    height = 800,
    background_color="white"
)
wordcloud = wordcloud.generate_from_frequencies(adj_counter)
array = wordcloud.to_array()
print(type(array)) # numpy.ndarray
print(array.shape) # (800, 800, 3)
fig = plt.figure(figsize=(10, 10))
plt.imshow(array, interpolation="bilinear")
plt.axis("off")
plt.show()
fig.savefig('wordcloud_without_axisoff_asdf.png')
