import nltk
import nltk.tokenize
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

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

def extract_patterns(tweets, senti_strength_words):
    patterns = {
        '-1': {
            '3' : {},
            '4' : {},
            '5' : {},
            '6' : {},
            '7' : {},
            '8' : {},
            '9' : {},
            '10': {}
        },
        '1' : {
            '3' : {},
            '4' : {},
            '5' : {},
            '6' : {},
            '7' : {},
            '8' : {},
            '9' : {},
            '10': {}
        }
    }
    for tweet in tweets:
        mood = tweet['mood']
        text = tweet['text']
        pattern = pattern_from_text(text, senti_strength_words)
        sub_patterns = patterns_for_different_lengths(pattern)
        for sub_pattern in sub_patterns:
            length = str(len(sub_pattern))
            sub_pattern_str = ' '.join(sub_pattern)
            pattern_hash = patterns[mood][length]
            if sub_pattern_str not in pattern_hash:
                pattern_hash[sub_pattern_str] = 0
            pattern_hash[sub_pattern_str] += 1
    delete_single_occurrences(patterns)
    delete_duplicates_accross_moods(patterns)
    return patterns

def pattern_from_text(text, senti_strength_words):
    words = nltk.tokenize.word_tokenize(text)
    tags = nltk.pos_tag(words)
    pattern = []
    for word_tag in tags:
        word = word_tag[0]
        tag  = word_tag[1]
        if tag in EI:
            prefix = 'NEUTRAL'
            if word in senti_strength_words:
                pos = int(senti_strength_words[word][0])
                neg = int(senti_strength_words[word][1])
                if pos > abs(neg):
                    prefix = 'POSITIVE'
                elif pos < abs(neg):
                    prefix = 'NEGATIVE'
            pattern.append('{}-{}'.format(prefix, hash_postag_expression[tag]))
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
    return pattern

def patterns_for_different_lengths(pattern):
    length = len(pattern)
    sub_patterns = []
    for i in range(3, 11):
        if i > length:
            break
        sub_patterns.append(pattern[0:i])
    return sub_patterns

def delete_single_occurrences(patterns):
    for mood in ['-1', '1']:
        for i in range(3, 11):
            pattern_hash = patterns[mood][str(i)]
            keys = []
            for key in pattern_hash.keys():
                if pattern_hash[key] == 1:
                    keys.append(key)
            for key in keys:
                del pattern_hash[key]

def delete_duplicates_accross_moods(patterns):
    for i in range(3, 11):
        length = str(i)
        neg = set(patterns['-1'][length].keys())
        pos = set(patterns['1'][length].keys())
        keys = set.intersection(neg, pos)
        for key in keys:
            del patterns['-1'][length][key]
            del patterns['1'][length][key]

def extract_features(text, patterns, words):
    features = {
        '-1': {
            '3' : 0,
            '4' : 0,
            '5' : 0,
            '6' : 0,
            '7' : 0,
            '8' : 0,
            '9' : 0,
            '10': 0
        },
        '1' : {
            '3' : 0,
            '4' : 0,
            '5' : 0,
            '6' : 0,
            '7' : 0,
            '8' : 0,
            '9' : 0,
            '10': 0
        }
    }
    pattern = pattern_from_text(text, words)
    sub_patterns = patterns_for_different_lengths(pattern)
    for sub_pattern in sub_patterns:
        length = str(len(sub_pattern))
        features['-1'][length] = similarity(sub_pattern, patterns['-1'][length])
        features['1'] [length] = similarity(sub_pattern, patterns['1'] [length])
    return features

def similarity(sub_pattern, patterns):
    K = 5
    length = len(sub_pattern)
    beta = (length - 1) / (length + 1)
    similarities = []
    for pattern_str in patterns:
        similarities.append(similarity0(sub_pattern, pattern_str))
    similarities.sort()
    similarities = similarities[0:K]
    return beta * sum(similarities)

def similarity0(sub_pattern, pattern_str):
    sub_pattern_str = ' '.join(sub_pattern)
    if sub_pattern_str is pattern_str:
        return 1
    pattern = pattern_str.split(' ')
    if len(set.intersection(set(sub_pattern), set(pattern))) == 0:
        return 0
    alpha = 0.03
    n = len(lcs(sub_pattern, pattern).split(' ')) - 1
    N = len(sub_pattern)
    return (alpha * n) / N

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + ' ' + result
            x -= 1
            y -= 1
    return result