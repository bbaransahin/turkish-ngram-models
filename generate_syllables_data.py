import syllables
import os

try:
  syllables_data_file = open('syllables_data', 'r')
  print('There is already a syllables data')
except FileNotFoundError:
  try:
    corpus_file = open('preprocessed_train', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a preprocessed data to syllabicate')
    print('FAIL')
    exit()

  print('Couldn\'t find syllables data, generating one..')
  syllables_data_file = open('syllables_data', 'w+')
  file_size = os.path.getsize('preprocessed_train')
  processed_bytes = 0
  while chunk := corpus_file.read(1024):
    if not chunk[-1].isspace():
      next_char = corpus_file.read(1)
      processed_bytes += 1
      while next_char and not next_char.isspace():
        chunk += next_char
        next_char = corpus_file.read(1)
        processed_bytes += 1

    syllables_chunk = syllables.syllabicate(chunk)

    for word in syllables_chunk:
      syllables_data_file.write(' '.join(word)+'\n')

    processed_bytes += len(chunk)
    progress = (processed_bytes / file_size) * 100
    print(f"Progress: {progress:.2f}%", end='\r')

  corpus_file.close()
  syllables_data_file.close()

print('                                                             ')
print('DONE')
