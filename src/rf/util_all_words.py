#!/usr/bin/python3

r = ['./data_tmp/train.csv','./data_tmp/test.csv']
w = ['./data_tmp/train/all_words.txt','./data_tmp/test/all_words.txt']

for i in range(2):
  with open(r[i], newline='', encoding='latin-1') as file:
    import csv
    csv_reader = csv.reader(file, delimiter=',')
    hashset = {}
    for row in csv_reader:
      words = row[5].split()
      for word in words:
        hashset[word] = None

  # clean
  import re
  keys_to_delete = []
  for key in sorted(hashset.keys()):
    if bool(re.search('^[!#@$].*', key)):
      keys_to_delete.append(key)

  for key in keys_to_delete:
    del hashset[key]

  out = '\n'.join(sorted(hashset.keys()))

  with open(w[i], 'w', encoding='latin-1') as file:
    file.write(out)
