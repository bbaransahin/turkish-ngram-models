# preprocess the corpus
print('preprocess the corpus..')
import preprocess
import os

try:
  open('preprocessed_wiki_00', 'r')
except FileNotFoundError:
  raw_corpus_file = open('wiki_00', 'r')
  preprocessed_file = open('preprocessed_wiki_00', 'w+')

  file_size = os.path.getsize('wiki_00')
  processed_bytes = 0
  while chunk := raw_corpus_file.read(1024):
    chunk = preprocess.remove_html_tags(chunk)
    chunk = preprocess.remove_punctuation(chunk)
    chunk = chunk.lower()

    preprocessed_file.write(chunk)

    processed_bytes += 1024
    progress = (processed_bytes / file_size) * 100
    print(f"Progress: {progress:.2f}%", end='\r')

  raw_corpus_file.close()
  preprocessed_file.close()

print('DONE')

# split the data
print('split the data..')
import train_test_split
train_test_split.split_data()

print('DONE')

# build n-gram tables
print('syllables..')
import generate_syllables_data

print('build n-gram tables..')
import build_ngram_tables
print('1-grams chars..')
build_ngram_tables.generate_1_grams_chars()
print('2-grams chars..')
build_ngram_tables.generate_2_grams_chars()
print('3-grams chars..')
build_ngram_tables.generate_3_grams_chars()
print('1-grams syllables..')
build_ngram_tables.generate_1_grams_syllables()
print('2-grams syllables..')
build_ngram_tables.generate_2_grams_syllables()
print('3-grams syllables..')
build_ngram_tables.generate_3_grams_syllables()

print('DONE')

# perplexity calculation
print('perplexity calculation..')
pass

print('PASS')

# random sentence generation
print('random sentence generation..')
import sentence_generation
import pickle

fi = open('chars_dict_1_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()
print('1-gram chars generation:')
print(sentence_generation.generate_1_grams_chars(data))
print('\n')

fi = open('chars_dict_2_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()
print('2-gram chars generation:')
print(sentence_generation.generate_2_grams_chars(data))
print('\n')

fi = open('chars_dict_3_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()
print('3-gram chars generation:')
print(sentence_generation.generate_3_grams_chars(data))
print('\n')

fi = open('syllables_dict_1_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()
print('1-gram syllables generation:')
print(sentence_generation.generate_1_grams_syllables(data))
print('\n')

fi = open('syllables_dict_2_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()
print('2-gram syllables generation:')
print(sentence_generation.generate_2_grams_syllables(data))
print('\n')

fi = open('syllables_dict_3_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()
print('3-gram syllables generation:')
print(sentence_generation.generate_3_grams_syllables(data))
print('\n')

print('DONE')
