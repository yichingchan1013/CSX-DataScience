
import os
import pickle
import jieba
import operator
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from datetime import datetime
from collections import Counter

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

from modules import *

font_path = 'msjh.ttc'
font = font_manager.FontProperties(fname='msjh.ttc',
                                   weight='bold',
                                   style='normal', size=16)



#打開爬蟲文本
with open('life_crawler.pkl', 'rb') as f:
    data = pickle.load(f)
    
data = data[::-1]
contents = [news['content'] for news in data]

#找出新詞
get_coshow(contents[:1000])[:10]

#載入自訂辭典
jieba.set_dictionary('dict.txt.big.txt')
jieba.load_userdict('userdict.txt')
stopwords = []
with open('stopwords.txt', 'r', encoding='UTF-8') as file:
    for each in file.readlines():
        stopwords.append(each.strip())
    stopwords.append(' ')


# add cutted dict to each news
for i in range(len(data)):
    current_content = data[i]['content']
    current_cutted = jieba.lcut(remove_punctuation(current_content))
    data[i]['cutted_dict'] = lcut_to_dict(current_cutted)
    
get_coshow(contents[:1000])[:10]


cutted_dict = get_cutted_dict(contents[:1000])
high_freq_pair = first_n_words(cutted_dict, 20)
high_freq_pair


cutted_dict = get_cutted_dict(contents)


# 可能人名
possible_name = first_n_words(cutted_dict, 1000, 3, 3)
possible_name[:10]
# 可能事件
possible_events = first_n_words(cutted_dict, 200, 4)
possible_events[:10]

#載入人名、事件
names = []
with open('names.txt', 'r', encoding='utf-8-sig') as f:
    names = f.read().split('\n')
events = []
with open('events.txt', 'r', encoding='utf-8-sig') as f:
    events = f.read().split('\n')



#製作文字雲
#非洲豬瘟
pig=get_wordcloud_of_keywords('豬', contents, 'pig.jpg')
pig.to_image()
pig.to_file('pig_cloud.png')


#校長遴選
ntu_president=get_wordcloud_of_keywords('校長', contents, 'ntu.jpg')
ntu_president.to_image()
ntu_president.to_file('ntu_president_cloud.png')






