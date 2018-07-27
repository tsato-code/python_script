import nltk

# 初回実行時のみ必要
# nltk.download('all')


sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

# 単語に分解
tokens = nltk.word_tokenize(sentence)
print(tokens)

# 形態素解析
tagged = nltk.pos_tag(tokens)
print(tagged)

# 文の構造
entities = nltk.chunk.ne_chunk(tagged)
print(entities)


"""
$ python test_nltk.py

['At', 'eight', "o'clock", 'on', 'Thursday', 'morning', 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'NN'), ('on', 'IN'), ('Thursday', 'NNP'), ('morning', 'NN'), ('Arthur', 'NNP'), ('did', 'VBD'), ("n't", 'RB'), ('feel', 'VB'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]
(S
  At/IN
  eight/CD
  o'clock/NN
  on/IN
  Thursday/NNP
  morning/NN
  (PERSON Arthur/NNP)
  did/VBD
  n't/RB
  feel/VB
  very/RB
  good/JJ
  ./.)
"""