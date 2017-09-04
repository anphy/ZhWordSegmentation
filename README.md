# ChineseWordSegmentation
Chinese word segmentation algorithm without corpus


## Explaination
When I need deal with some chinese texts, I found this module [ChineseWordSegmentation](https://github.com/Moonshile/ChineseWordSegmentation). 

So I did an  adjustment to fit my needs. 

Since the it is not maintained by it's author, I, though a newbee in NLP, want to make it a more useful tool for processing chinese texts.


## Install:
Until now, I test it on my pc 
+ version: py3.6
+ do : fork this git to your local dir
+ run this: python3 setup.py install


## Usage
``` python
from zhseg import *
doc = u'十四是十四四十是四十，十四不是四十，四十不是十四'
ws = wordseg.WordSegment(doc, max_word_len=2, min_aggregation=1, min_entropy=0.5)
ws.segSentence(doc)
```

This will generate words

`十四 是 十四 四十 是 四十 ， 十四 不是 四十 ， 四十 不是 十四`

In fact, `doc` should be a long enough document string for better results. In that condition, the min_aggregation should be set far greater than 1, such as 50, and min_entropy should also be set greater than 0.5, such as 1.5.

Besides, both input and output of this function should be decoded as unicode.

`WordSegment.segSentence` has an optional argument `method`, with values `WordSegment.L`, `WordSegment.S` and `WordSegment.ALL`, means

+ `WordSegment.L`: if a long word that is combinations of several shorter words found, given only the long word.
+ `WordSegment.S`: given the several shorter words.
+ `WordSegment.ALL`: given both the long and the shorters.

## Reference

Thanks Matrix67's [article](http://www.matrix67.com/blog/archives/5044)


Well done, do report me if any bad things happended

## plans:
[x] add concurrent soupport

[x] add read and save datasets, as you read more you get more words

[x] add more algorithm