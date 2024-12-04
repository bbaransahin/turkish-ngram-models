import preprocess

try:
  fi = open('preprocessed_wiki_00', 'r')
  print('There is already a preprocessed data')
except FileNotFoundError:
  print('Couldn\'t find preprocessed data, generating one..')
  corpus_file = open('wiki_00', 'r')
  corpus = corpus_file.read()
  print(len(corpus))

  fi = open('preprocessed_wiki_00', 'w+')

  corpus = preprocess.remove_html_tags(corpus)
  corpus = preprocess.remove_punctuation(corpus)
  corpus = corpus.lower()

  fi.write(corpus)

  corpus_file.close()

fi.close()
print('DONE')
