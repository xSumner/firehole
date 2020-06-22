# FireHole

[英文](https://github.com/xSumner/firehole/README.md) | [docker]()



FireHole 是一个为烽火IAO的数据分析师量身定做的工具包。

- 网址（内网）: 
- 项目地址：https://github.com/xSumner/firehole
- 上报Bug：https://github.com/xSumner/firehole/issues



## 安装

```
pip install firehole
```

FireHole 需要Python 3.4 或更高版本。



## 快速上手

### 引入 FireHole

```python
import firehole as fh
# 由于FireHole基于numpy，因此也要引入
import numpy as np
```



### 多指标综合评价算法

使用以下方法为多指标综合系统进行评分：

- 层次分析法 (AHP)
- 熵权法
- 变异系数法
- ......

#### 1. 层次分析法（AHP)

```python
import json
import firehole as fh

model = {
    "name": "Sample Model",
    "method": "approximate",
    "criteria": ["critA", "critB", "critC"],
    "subCriteria": {
        "critA": ["subCritA", "subCritB"]
    },
    "alternatives": ["altA", "altB", "altC"],
    "preferenceMatrices": {
        "criteria": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ],
        "subCriteria:critA": [
            [1, 1],
            [1, 1]
        ],
        "alternatives:subCritA": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ],
        "alternatives:subCritB": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ],
        "alternatives:critB": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ],
        "alternatives:critC": [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    }
}

ahp_model = fh.parse(model)
priorities = ahp_model.get_priorities()
```



#### 2. 熵权法

```python
>>> li = [[100, 90, 100, 84, 90, 100, 100, 100, 100],
          [100, 100, 78.6, 100, 90, 100, 100, 100, 100],
          [75, 100, 85.7, 100, 90, 100, 100, 100, 100],
          [100, 100, 78.6, 100, 90, 100, 94.4, 100, 100],
          [100, 90, 100, 100, 100, 90, 100, 100, 80],
          [100, 100, 100, 100, 90, 100, 100, 85.7, 100],
          [100, 100, 78.6, 100, 90, 100, 55.6, 100, 100],
          [87.5, 100, 85.7, 100, 100, 100, 100, 100, 100],
          [100, 100, 92.9, 100, 80, 100, 100, 100, 100],
          [100, 90, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 92.9, 100, 90, 100, 100, 100, 100]]
>>> # convert list into numpy array
>>> li = np.array(li)
>>> # calculation by entropy method
>>> entropy = fh.Entropy()
>>> rlt = entropy.entropy(li)
>>> 
>>> print(rlt['entropy'])
[0.9912947 0.99752157 0.98629816 0.99731237 0.9946718 0.99902487 0.95993528 0.9978992 0.99556829]
>>> print(rlt['weight'])
[0.10817562 0.03079802 0.17026463 0.03339765 0.06621039 0.0121174 0.49786068 0.02610541 0.0550702 ]
>>> print(rlt['score'])
[1.09856723 0.31796876 1.4625885 0.35533899 0.59410402 0.1305623 4.91581354 0.27875173 0.58096578]
```



#### 3. 变异系数法

```python
>>> a = [[3051, 20.4, 30.1, 0.5250, 31.1, 9.5, 70.1, 82.8, 6, 2],
         [20763, 0.1, 84.1, 0.9969, 100, -1.7, 78.6, 92.9, 28, 1.3],
         [2407, 16.7, 39.9, 0.5504, 38.8, 15.6, 65.6, 85.7, 7, 0.2],
         [5121, 24.9, 38.4, np.nan, 60.6, 16.5, 69.5, 74.6, 18, 0.9],
         [16861, np.nan, np.nan, 0.9769, 91, 15.7, 77.9, 95.7, 44, 4.6],
         [23592, 1.9, 60.3, 0.9473, 78.5, 2.1, 80, 99, 43, 1.8],
         [4317, 12.8, 60.3, np.nan, 56.4, 4.4, 67.9, 99, 32, 3.5],
         [13286, 5.8, 51.2, 0.8824, 80.4, 8.7, 72.6, 97.5, 60, 1.1],
         [7699, 12.6, 42, 0.8120, 55.9, 20.5, 72.2, 86.4, 11, 0.5],
         [3725, 20.6, 47.3, 0.6012, 56.8, 22.3, 68.6, 94.8, 35, 0.6],
         [25295, 0.2, 65.2, 0.9979, 100, 8.6, 77.3, 91.8, 39, 1.7],
         [2945, 22.4, 51.1, 0.5843, 23, 11.5, 73.3, 91.1, 5, 4.2],
         [5524, 9.6, 49.5, 0.4875, 21, 10.2, 68.9, 95, 21, 2.9],
         [6594, 17.4, 54.7, 0.5658, 72.9, 14.8, 69.3, 84, 18, 1.5],
         [3146, 17.3, 51.1, np.nan, 44.9, 17.2, 66.7, 53.7, np.nan, 2.1],
         [8296, 4.2, 62.2, np.nan, 52.9, 15.9, 53.2, 84.6, 19, 0.6],
         [22814, np.nan, np.nan, 0.9651, 76.9, 4.4, 79.1, 99, 90, 2.1],
         [7450, 5.5, 68.6, 0.8021, 74, 22.4, 72.3, 90.8, 16, 1.2],
         [29240, 1.8, 71.8, 0.9733, 76.8, 5.8, 76.8, 99, 81, 2.6],
         [11728, 6, 65.6, 0.9849, 89.3, 11.7, 73.1, 96.7, 42, 2.7],
         [6460, 8.3, 62.3, 0.7581, 80.1, 13.0, 67, 84.5, 12, 1.3],
         [5706, 4.2, 49.3, 0.8921, 86.3, 20.5, 72.6, 92, 25, 2.4],
         [6314, 16, 44, np.nan, 70.6, -4.3, 68.1, 99.5, 44, 4.3],
         [4683, 14.5, 57, np.nan, 69, -6.4, 71.3, 98.2, 41, 3.5],
         [12197, 4.3, 58, 0.9535, 74.6, -1.8, 74.1, 99, 23, 2.9],
         [21214, 2.3, 71.5, np.nan, 75.2, 3.4, 78.2, 99, 52, 2.9],
         [22026, 1.1, 44.2, 0.9717, 87.1, -0.7, 77.3, 99, 45, 3.4],
         [20365, 2.8, 66.4, np.nan, 66.8, -0.1, 78.3, 98.3, 43, 5.5],
         [22325, np.nan, np.nan, 0.9681, 89.2, 3.1, 78, 99, 50, 2.6],
         [7543, 5.6, 61.6, 0.8089, 64.8, 0.6, 72.7, 99.7, 24, 2.3],
         [5572, 19.5, 36.1, 0.6003, 55.7, -1.3, 70.2, 97.9, 23, 1.8],
         [6180, 7.5, 55.7, np.nan, 77, -4.7, 66.7, 99.5, 41, 4.6],
         [15960, 3.5, 25.1, 0.9239, 77.2, 0.1, 78.1, 97.4, 51, 4.2],
         [20314, 1.8, 66.7, 0.9835, 89.4, 1.3, 77.3, 99, 50, 1.6],
         [3130, 13.8, 48.4, 0.7388, 67.8, -6.3, 69.1, 99.6, 42, 4.5],
         [21795, 3.2, 70.6, 0.9524, 84.7, 6.5, 78.3, 99, 76, 2.5],
         [16084, np.nan, np.nan, 0.9148, 85.6, 7.9, 77.1, 99, 59, 2.1]]
>>> a = np.array(a)
>>> target = np.array([22930, 2, 63, 0.9580, 76, 4, 77, 97.5, 58, 2.5], dtype='float')
>>> pos_neg = np.array([1, -1, 1, 1, 1, -1, 1, 1, 1, 1], dtype='float')
>>> cov = fh.COV()
>>> result = cov.comprehensive(data=a, target=target, pos_neg=pos_neg, decimals=2)
>>> print(result)
[ 0.35  3.3   0.25  0.3   0.63  1.18  0.64  0.62  0.32  0.33  2.36  0.45
  0.46  0.4   0.3   0.39  0.81  0.43  1.04  0.64  0.43  0.52  0.25  0.28
 -0.03  0.98 -0.54 -9.31  0.85  2.12 -0.45  0.31 10.72  1.48  0.35  0.88
  0.6 ]
```



### 关键词抽取

基于Trie字典数据结构，从文本中提取关键词。

#### 1. 提取关键词

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_processor.add_keyword('Big Apple', 'New York')
>>> keyword_processor.add_keyword('Bay Area')
>>> keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
>>> keywords_found
>>> # ['New York', 'Bay Area']
```

```python
import firehole as fh
keyword_processor = fh.KeywordProcessor()
keyword_processor.add_keyword('口号')
keyword_processor.add_keyword('横幅')
keywords_found = keyword_processor.extract_keywords('他边喊口号边走近了那个建筑，并拉起了横幅。')
keywords_found
# ['口号', '横幅']
```

#### 2. 替换关键词

```python
>>> keyword_processor.add_keyword('New Delhi', 'NCR region')
>>> new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
>>> new_sentence
>>> # 'I love New York and NCR region.'
```

#### 3. 大小写敏感设置

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor(case_sensitive=True)
>>> keyword_processor.add_keyword('Big Apple', 'New York')
>>> keyword_processor.add_keyword('Bay Area')
>>> keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
>>> keywords_found
>>> # ['Bay Area']
```

#### 4. 关键词提取范围

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_processor.add_keyword('Big Apple', 'New York')
>>> keyword_processor.add_keyword('Bay Area')
>>> keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.', span_info=True)
>>> keywords_found
>>> # [('New York', 7, 16), ('Bay Area', 21, 29)]
```

#### 5. 关键词提取额外信息

```python
>>> import firehole as fh
>>> kp = fh.KeywordProcessor()
>>> kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
>>> kp.add_keyword('Delhi', ('Location', 'Delhi'))
>>> kp.extract_keywords('Taj Mahal is in Delhi.')
>>> # [('Monument', 'Taj Mahal'), ('Location', 'Delhi')]
>>> # NOTE: replace_keywords feature won't work with this.
```

#### 6. 关键词无标准名

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_processor.add_keyword('Big Apple')
>>> keyword_processor.add_keyword('Bay Area')
>>> keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
>>> keywords_found
>>> # ['Big Apple', 'Bay Area']
```

#### 7. 同时添加多个关键词

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_dict = {
>>>     "java": ["java_2e", "java programing"],
>>>     "product management": ["PM", "product manager"]
>>> }
>>> # {'clean_name': ['list of unclean names']}
>>> keyword_processor.add_keywords_from_dict(keyword_dict)
>>> # Or add keywords from a list:
>>> keyword_processor.add_keywords_from_list(["java", "python"])
>>> keyword_processor.extract_keywords('I am a product manager for a java_2e platform')
>>> # output ['product management', 'java']
```

#### 8. 移除关键词

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_dict = {
>>>     "java": ["java_2e", "java programing"],
>>>     "product management": ["PM", "product manager"]
>>> }
>>> keyword_processor.add_keywords_from_dict(keyword_dict)
>>> print(keyword_processor.extract_keywords('I am a product manager for a java_2e platform'))
>>> # output ['product management', 'java']
>>> keyword_processor.remove_keyword('java_2e')
>>> # you can also remove keywords from a list/ dictionary
>>> keyword_processor.remove_keywords_from_dict({"product management": ["PM"]})
>>> keyword_processor.remove_keywords_from_list(["java programing"])
>>> keyword_processor.extract_keywords('I am a product manager for a java_2e platform')
>>> # output ['product management']
```

#### 9. 检查关键词数量

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_dict = {
>>>     "java": ["java_2e", "java programing"],
>>>     "product management": ["PM", "product manager"]
>>> }
>>> keyword_processor.add_keywords_from_dict(keyword_dict)
>>> print(len(keyword_processor))
>>> # output 4
```

#### 10. 检查关键词是否被包含

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_processor.add_keyword('j2ee', 'Java')
>>> 'j2ee' in keyword_processor
>>> # output: True
>>> keyword_processor.get_keyword('j2ee')
>>> # output: Java
>>> keyword_processor['colour'] = 'color'
>>> keyword_processor['colour']
>>> # output: color
```

#### 11. 获取全部的关键词词典

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_processor.add_keyword('j2ee', 'Java')
>>> keyword_processor.add_keyword('colour', 'color')
>>> keyword_processor.get_all_keywords()
>>> # output: {'colour': 'color', 'j2ee': 'Java'}
```

#### 12. 设置分词规则（英文）

```python
>>> import firehole as fh
>>> keyword_processor = fh.KeywordProcessor()
>>> keyword_processor.add_keyword('Big Apple')
>>> print(keyword_processor.extract_keywords('I love Big Apple/Bay Area.'))
>>> # ['Big Apple']
>>> keyword_processor.add_non_word_boundary('/')
>>> print(keyword_processor.extract_keywords('I love Big Apple/Bay Area.'))
>>> # []
```



### 文本相似度

计算不同文本之间的相似度。

#### 1. BM25

- OKapi BM25
- BM25L
- BM25+

```python
>>> import firehole as fh
>>> corpus = ["Hello there good man!", 
              "It is quite windy in London", 
              "How is the weather today?"]
>>> tokenized_corpus = [doc.split(" ") for doc in corpus]
>>> bm25 = fh.BM25_okapi(tokenized_corpus)
<firehole.algorithms.similarity.rank_bm25.BM25Okapi at 0x13a49c88>
>>> query = "windy London"
>>> tokenized_query = query.split(" ")
>>> doc_scores = bm25.get_scores(tokenized_query)
# array([0.    , 0.93729472, 0.    ])
>>> bm25.get_top_n(tokenized_query, corpus, n=1)
# ['It is quite windy in London']
```

```python
import firehole as fh
import jieba
corpus = ["他手执横幅走了进来", 
          "他走了进来", 
          "横幅上写着很多的字"]
tokenized_corpus = [jieba.lcut(doc, cut_all=False, HMM=True) for doc in corpus]
bm25 = fh.BM25Okapi(tokenized_corpus)
query = "他有一个横幅"
tokenized_query = jieba.lcut(query, cut_all=False, HMM=True)
doc_scores = bm25.get_scores(tokenized_query)
print(doc_scores)
# [0.04147104 0.02453117 0.01924653]
bm25.get_top_n(tokenized_query, corpus, n=1)
# ['他手执横幅走了进来']
```



#### 2. Simhash

计算Simhash的值：

```python
import re
import firehole as fh

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

text1 = 'How are you? I am fine. Thanks.'
text2 = 'How are u, I am fine. Thanks.'
text3 = 'How r u?I am fine. Thanks.'

print('%x' % fh.Simhash(get_features(text1)).value)
print('%x' % fh.Simhash(get_features(text2)).value)
print('%x' % fh.Simhash(get_features(text3)).value)
```

```python
import re
import firehole as fh

def get_features(s):
    width = 3
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

text1 = '他手执横幅走了进来。'
text2 = '他走了进来。'
text3 = '横幅上写着很多的字'

print('%x' % fh.Simhash(get_features(text1)).value)
print('%x' % fh.Simhash(get_features(text2)).value)
print('%x' % fh.Simhash(get_features(text3)).value)
# f8b6c362c7552669
# fa377b62e7d9a81c
# 98965516240442ee
```



计算两个Simhash的距离：

```python
import re
import firehole as fh

print(fh.Simhash('aa').distance(fh.Simhash('bb')))
print(fh.Simhash('aa').distance(fh.Simhash('aa')))

hash1 = fh.Simhash(u'I am very happy'.split())
hash2 = fh.Simhash(u'I am very sad'.split())
print(hash1.distance(hash2))
```

```python
import re
import firehole as fh

print(fh.Simhash('政府').distance(fh.Simhash('大楼')))
print(fh.Simhash('政府').distance(fh.Simhash('政府')))

hash1 = fh.Simhash(jieba.lcut("我很开心", cut_all=False, HMM=True))
hash2 = fh.Simhash(jieba.lcut("我很忧伤", cut_all=False, HMM=True))
print(hash1.distance(hash2))
```



使用SimhashIndex来高效查询最相似的文本：

```python
import re
import firehole as fh

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

data = {
    1: u'How are you? I Am fine. blar blar blar blar blar Thanks.',
    2: u'How are you i am fine. blar blar blar blar blar than',
    3: u'This is simhash test.',
}
objs = [(str(k), fh.Simhash(get_features(v))) for k, v in data.items()]
index = fh.SimhashIndex(objs, k=3)

print(index.bucket_size())

s1 = fh.Simhash(get_features(u"How are you i am fine. blar blar blar blar blar thank"))
print(index.get_near_dups(s1))

index.add("4", s1)
print(index.get_near_dups(s1))
```









