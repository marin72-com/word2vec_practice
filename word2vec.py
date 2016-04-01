# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys

# output log
logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)

def load_wakati(filename):
    sentences = word2vec.Text8Corpus(filename)
    return word2vec.Word2Vec(sentences, size=200, min_count=20, window=10)

def save_model(model, filename='sample.model'):
    model.save(filename)

def get_word2vec_model():
    filename = 'tweets-wakati.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    model = load_wakati(filename)
    save_model(model, filename + '.model')
    return model
    
def get_similar_words(posi, nega=[], n=10):
    model = get_word2vec_model()
    cnt = 1
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print cnt, ' ', r[0], ' ', r[1]
        cnt += 1

if __name__ == '__main__':
    print "Load finish"
    get_similar_words(['twitter'])

