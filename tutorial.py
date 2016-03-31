# -*- coding:utf-8 -*- 
from gensim import corpora, models, similarities 
def parse(doc):
    stoplist = set('for a of the and to in'.split())
    texts = [word for word in doc.lower().split() if word not in stoplist]
    return texts

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

texts = [[w for w in parse(doc)] for doc in documents]
#print texts

all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

#print texts
dictionary = corpora.Dictionary(texts)
dictionary.save('text.dict')    # binary
dictionary.save_as_text('text.txt') #textfile 

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('corpora.mm', corpus)

# new dictionary
new_doc = "Human computer interaction"
#print parse(new_doc)
new_vec = dictionary.doc2bow(parse(new_doc))
#print new_vec

# measure similarities
index = similarities.docsim.SparseMatrixSimilarity(corpus, num_features=len(dictionary))
print (sorted(enumerate(index[new_vec]), reverse=True, key=lambda x:x[1])[:10])

# adopt model
m = models.TfidfModel(corpus)
# toransformation between word-document co-occurrence matrix
# m[corpus[0]] = [(0, 0.5773502691896257), (1, 0.5773502691896257), (2, 0.5773502691896257)]
corpus = m[corpus]

# adopt topic model
m = models.LdaModel(corpus, id2word = dictionary, num_topics = 5)

for i in range(0, m.num_topics):
    print (m.show_topics(formatted=True)[i])


