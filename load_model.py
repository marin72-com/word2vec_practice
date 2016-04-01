#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
from gensim.models import word2vec
import logging
import sys

model = word2vec.Word2Vec.load("sample.model")

def s(posi, nega=[], n=10):
    cnt = 1
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print cnt, ' ', r[0], ' ', r[1]
        cnt += 1

if __name__ == '__main__':
    word = sys.argv[1]
    word = unicode(word, 'utf-8')
    s([word])

