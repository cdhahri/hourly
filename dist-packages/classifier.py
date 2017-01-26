
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

def patterns(text_list):
  patterns = []
  for text in text_list:
    pattern = []
    words = nltk.tokenize.word_tokenize(text)
    tags = nltk.pos_tag(words)
    for word_tag in tags:
      word = word_tag[0]
      tag = word_tag[1]
      if tag in EI:
        # polarity with senti strength
        # look up
        pattern.append(hash_postag_expression[tag])
      elif tag in CI:
        # lemmatization
        pattern.append(word)
      elif tag in GFI:
        # look up
        pattern.append(hash_postag_expression[tag])
      elif tag in ignore:
        continue
      else:
        print('Tag {} not found in any of three classes'.format(tag))
        import sys
        sys.exit(1)
    patterns.append(pattern)
  return patterns