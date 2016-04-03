# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys
import csv
import MeCab
import re
import os.path

# output log
logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)

def create_wakati(input_filename='tweets.csv', output_filename='tweets-wakati.txt'):
    tagger = MeCab.Tagger('-Owakati')
    fo = file (output_filename, 'w')
    with open(input_filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        print header

        for line in reader:
            line = line[5]
            line = re.sub('https?://.*', '', line)
            fo.write(tagger.parse(line))

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
    filename = 'tweets-wakati.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    # もし、wakati ファイルがなかったら作る
    if not os.path.isfile(filename):
        create_wakati('tweets/tweets.csv', filename)

    print "Load finish"

    wvm = Word2VecModel(filename)
    wvm.get_similar_words('twitter')

