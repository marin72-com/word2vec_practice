# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys

# output log
logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)

class Word2VecModel:
    def __init__(self, filename='tweets-wakati.txt'):
        self.model = self.load_wakati(filename)
    
    def load_wakati(self, filename):
        sentences = word2vec.Text8Corpus(filename)
        return word2vec.Word2Vec(sentences, size=200, min_count=20, window=10)
    
    def save_model(self, filename='sample.model'):
        self.model.save(filename)
    
    def get_word2vec_model(self):
        return self.model
        
    def get_similar_words(self, posi, nega=[], n=10):
        cnt = 1
        result = self.model.most_similar(positive = posi, negative = nega, topn = n)
        print posi
        for r in result:
            print cnt, ' ', r[0], ' ', r[1]
            cnt += 1

if __name__ == '__main__':
    print "Load finish"

    filename = 'tweets-wakati.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    wvm = Word2VecModel(filename)
    wvm.get_similar_words('twitter')

