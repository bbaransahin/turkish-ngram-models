import os

def split_data():
  try:
    corpus_file = open('preprocessed_wiki_00', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a preprocessed data to split')
    print('FAIL')
    exit()

  file_size = os.path.getsize('preprocessed_wiki_00')
  chunk_size = int(file_size*5/100)+1

  test_corpus_file = open('preprocessed_test', 'w+')
  test_corpus_file.write(corpus_file.read(chunk_size))
  test_corpus_file.close()

  train_corpus_file = open('preprocessed_train', 'w+')
  while chunk := corpus_file.read(chunk_size):
    train_corpus_file.write(chunk)
  train_corpus_file.close()

  print('Total data size =', os.path.getsize('preprocessed_wiki_00'))
  print('Test data size =', os.path.getsize('preprocessed_test'))
  print('Train data size =', os.path.getsize('preprocessed_train'))
