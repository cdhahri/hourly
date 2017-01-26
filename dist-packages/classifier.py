
EI = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

CI = ['CC', 'DT', 'EX', 'IN', 'MD', 'PDT', 'POS', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'WDT', 'WP', 'WP$', 'WRB']

GFI = ['CD', 'FW', 'LS', 'NNP', 'NNPS', 'PRP', 'PRP$', 'SYM', 'UH']

hash_postag_expression = {
  'CD': 'CARDINAL',

  'FW': 'FOREIGNWORD',

  'UH': 'INTERJECTION',

  'LS': 'LISTMARKER',

  'NN'  : 'NOUN',
  'NNS' : 'NOUN',
  'NNP' : 'NOUN',
  'NNPS': 'NOUN',

  'PRP' : 'INTERJECTION',
  'PRP$': 'INTERJECTION',

  'MD': 'MODAL',

  'RB' : 'ADVERB',
  'RBR': 'ADVERB',
  'RBS': 'ADVERB',

  'VB' : 'VERB',
  'VBD': 'VERB',
  'VBG': 'VERB',
  'VBN': 'VERB',
  'VBP': 'VERB',
  'VBZ': 'VERB',

  'WDT': 'WHDETERMINER',
  'WP' : 'WHDETERMINER',
  'WP$': 'WHDETERMINER',
  'WRB': 'WHDETERMINER',

  'SYM': 'SYMBOL',

  'JJ' : 'ADJECTIVE',
  'JJR': 'ADJECTIVE',
  'JJS': 'ADJECTIVE',
}

ignore = ['.', ',', ':', '#', '$', '(', ')', '\'\'', '``']

import nltk
import nltk.tokenize
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

def patterns(text_list, senti_strength_words):
  patterns = []
  for text in text_list:
    pattern = []
    words = nltk.tokenize.word_tokenize(text)
    tags = nltk.pos_tag(words)
    for word_tag in tags:
      word = word_tag[0]
      tag = word_tag[1]
      if tag in EI:
        prefix = ''
        if word in senti_strength_words:
          pos = int(senti_strength_words[word][0])
          neg = int(senti_strength_words[word][1])
          if pos > abs(neg):
            prefix = 'POS'
          elif pos < abs(neg):
            prefix = 'NEG'
        pattern.append('{}{}'.format(prefix, hash_postag_expression[tag]))
      elif tag in CI:
        lemma = wordnet_lemmatizer.lemmatize(word)
        pattern.append(lemma)
      elif tag in GFI:
        pattern.append(hash_postag_expression[tag])
      elif tag in ignore:
        continue
      else:
        print('Tag {} not found in any of three classes'.format(tag))
        import sys
        sys.exit(1)
    patterns.append(pattern)

  patterns_hash = {}
  for pattern in patterns:
    pattern2 = ' '.join(pattern)
    if pattern2 not in patterns_hash:
      patterns_hash[pattern2] = 0
    patterns_hash[pattern2] = patterns_hash[pattern2] + 1

  patterns = []
  for key in sorted(patterns_hash.keys()):
    if patterns_hash[key] > 1:
      print('{}: {}'.format(key, patterns_hash[key]))
      patterns.append(key)
  return patterns
