import pickle
from tqdm import tqdm
import os

def generate_1_grams_chars():
  try:
    preprocessed_data_file = open('preprocessed_train', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a preprocessed data to generate dict')
    print('FAIL')
    exit()

  try:
    chars_dict_file = open('chars_dict_1_grams.pkl', 'rb')
    print('There is already a chars dict file')
  except FileNotFoundError:
    print('Couldn\'t find chars dict file, generating one..')
    chars_dict = {}
    file_size = os.path.getsize('preprocessed_train')
    processed_bytes = 0
    while chunk := preprocessed_data_file.read(1024):
      for ch in chunk:
        if (not ch in chars_dict):
          chars_dict[ch] = 0
        chars_dict[ch] += 1
      processed_bytes += len(chunk)
      progress = (processed_bytes / file_size) * 100
      print(f"Progress: {progress:.2f}%", end='\r')

    chars_dict_file = open('chars_dict_1_grams.pkl', 'wb')
    pickle.dump(chars_dict, chars_dict_file)
    chars_dict_file.close()

    print(chars_dict)

  print('DONE')

def generate_2_grams_chars():
  try:
    preprocessed_data_file = open('preprocessed_train', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a preprocessed data to generate dict')
    print('FAIL')
    exit()

  try:
    chars_dict_file = open('chars_dict_2_grams.pkl', 'rb')
    print('There is already a chars dict file')
  except FileNotFoundError:
    print('Couldn\'t find chars dict file, generating one..')
    chars_dict = {}
    chars_buffer = []
    file_size = os.path.getsize('preprocessed_train')
    processed_bytes = 0
    while chunk := preprocessed_data_file.read(1024):
      for ch in chunk:
        chars_buffer.append(ch)
        if (len(chars_buffer) > 2):
          if (not chars_buffer[0] in chars_dict):
            chars_dict[chars_buffer[0]] = {}
          if (not chars_buffer[1] in chars_dict[chars_buffer[0]]):
            chars_dict[chars_buffer[0]][chars_buffer[1]] = 0
          chars_dict[chars_buffer[0]][chars_buffer[1]] += 1

          chars_buffer.pop(0)

      if (not chars_buffer[0] in chars_dict):
        chars_dict[chars_buffer[0]] = {}
      if (not chars_buffer[1] in chars_dict[chars_buffer[0]]):
        chars_dict[chars_buffer[0]][chars_buffer[1]] = 0
      chars_dict[chars_buffer[0]][chars_buffer[1]] += 1

      processed_bytes += len(chunk)
      progress = (processed_bytes / file_size) * 100
      print(f"Progress: {progress:.2f}%", end='\r')

    chars_dict_file = open('chars_dict_2_grams.pkl', 'wb')
    pickle.dump(chars_dict, chars_dict_file)
    chars_dict_file.close()

    print(chars_dict)

  print('DONE')

def generate_3_grams_chars():
  try:
    preprocessed_data_file = open('preprocessed_train', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a preprocessed data to generate dict')
    print('FAIL')
    exit()

  try:
    chars_dict_file = open('chars_dict_3_grams.pkl', 'rb')
    print('There is already a chars dict file')
  except FileNotFoundError:
    print('Couldn\'t find chars dict file, generating one..')
    chars_dict = {}
    chars_buffer = []
    file_size = os.path.getsize('preprocessed_train')
    processed_bytes = 0
    while chunk := preprocessed_data_file.read(1024):
      for ch in chunk:
        chars_buffer.append(ch)
        if (len(chars_buffer) > 3):
          key = tuple(chars_buffer[:2])
          if (not key in chars_dict):
            chars_dict[key] = {}
          if (not chars_buffer[2] in chars_dict[key]):
            chars_dict[key][chars_buffer[2]] = 0
          chars_dict[key][chars_buffer[2]] += 1

          chars_buffer.pop(0)

      key = tuple(chars_buffer[:2])
      if (not key in chars_dict):
        chars_dict[key] = {}
      if (not chars_buffer[2] in chars_dict[key]):
        chars_dict[key][chars_buffer[2]] = 0
      chars_dict[key][chars_buffer[2]] += 1

      processed_bytes += len(chunk)
      progress = (processed_bytes / file_size) * 100
      print(f"Progress: {progress:.2f}%", end='\r')

    chars_dict_file = open('chars_dict_3_grams.pkl', 'wb')
    pickle.dump(chars_dict, chars_dict_file)
    chars_dict_file.close()

    print(chars_dict)

  print('DONE')

def generate_1_grams_syllables():
  try:
    syllables_data_file = open('syllables_data', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a syllables data to generate dict')
    print('FAIL')
    exit()

  try:
    syllables_dict_file = open('syllables_dict_1_grams.pkl', 'rb')
    print('There is already a syllables dict file')
  except FileNotFoundError:
    print('Couldn\'t find syllables dict file, generating one..')
    syllables_dict = {}
    for word in tqdm(syllables_data_file): # every line is a word
      word = word.split(' ')
      for i in range(len(word)):
        if (i == len(word)-1):
          if (not word[i][:-1]+' ' in syllables_dict):
            syllables_dict[word[i][:-1]+' '] = 0
          syllables_dict[word[i][:-1]+' '] += 1
        else:
          if (not word[i] in syllables_dict):
            syllables_dict[word[i]] = 0
          syllables_dict[word[i]] += 1
      
    syllables_dict_file = open('syllables_dict_1_grams.pkl', 'wb')
    pickle.dump(syllables_dict, syllables_dict_file)
    syllables_dict_file.close()

    print(syllables_dict)

  print('DONE')

def generate_2_grams_syllables():
  try:
    syllables_data_file = open('syllables_data', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a syllables data to generate dict')
    print('FAIL')
    exit()

  try:
    syllables_dict_file = open('syllables_dict_2_grams.pkl', 'rb')
    print('There is already a syllables dict file')
  except FileNotFoundError:
    print('Couldn\'t find syllables dict file, generating one..')
    syllables_dict = {}
    syllables_buffer = []
    for word in tqdm(syllables_data_file): # every line is a word
      word = word.split(' ')
      for i in range(len(word)):
        if (i == len(word)-1):
          syllables_buffer.append(word[i][:-1]+' ')
        else:
          syllables_buffer.append(word[i])
        if (len(syllables_buffer) > 2):
          if (not syllables_buffer[0] in syllables_dict):
            syllables_dict[syllables_buffer[0]] = {}
          if (not syllables_buffer[1] in syllables_dict[syllables_buffer[0]]):
            syllables_dict[syllables_buffer[0]][syllables_buffer[1]] = 0
          syllables_dict[syllables_buffer[0]][syllables_buffer[1]] += 1

          syllables_buffer.pop(0)
      
    if (not syllables_buffer[0] in syllables_dict):
      syllables_dict[syllables_buffer[0]] = {}
    if (not syllables_buffer[1] in syllables_dict[syllables_buffer[0]]):
      syllables_dict[syllables_buffer[0]][syllables_buffer[1]] = 0
    syllables_dict[syllables_buffer[0]][syllables_buffer[1]] += 1

    syllables_dict_file = open('syllables_dict_2_grams.pkl', 'wb')
    pickle.dump(syllables_dict, syllables_dict_file)
    syllables_dict_file.close()

    print(syllables_dict)

  print('DONE')

def generate_3_grams_syllables():
  try:
    syllables_data_file = open('syllables_data', 'r')
  except FileNotFoundError:
    print('Couldn\'t find a syllables data to generate dict')
    print('FAIL')
    exit()

  try:
    syllables_dict_file = open('syllables_dict_3_grams.pkl', 'rb')
    print('There is already a syllables dict file')
  except FileNotFoundError:
    print('Couldn\'t find syllables dict file, generating one..')
    syllables_dict = {}
    syllables_buffer = []
    for word in tqdm(syllables_data_file): # every line is a word
      word = word.split(' ')
      for i in range(len(word)):
        if (i == len(word)-1):
          syllables_buffer.append(word[i][:-1]+' ')
        else:
          syllables_buffer.append(word[i])
        if (len(syllables_buffer) > 3):
          if (not tuple(syllables_buffer[:2]) in syllables_dict):
            syllables_dict[tuple(syllables_buffer[:2])] = {}
          if (not syllables_buffer[2] in
            syllables_dict[tuple(syllables_buffer[:2])]):
            syllables_dict[tuple(syllables_buffer[:2])][syllables_buffer[2]]=0
          syllables_dict[tuple(syllables_buffer[:2])][syllables_buffer[2]]+=1

          syllables_buffer.pop(0)
      
    if (not tuple(syllables_buffer[:2]) in syllables_dict):
      syllables_dict[tuple(syllables_buffer[:2])] = {}
    if (not syllables_buffer[2] in
      syllables_dict[tuple(syllables_buffer[:2])]):
      syllables_dict[tuple(syllables_buffer[:2])][syllables_buffer[2]]=0
    syllables_dict[tuple(syllables_buffer[:2])][syllables_buffer[2]]+=1

    syllables_dict_file = open('syllables_dict_3_grams.pkl', 'wb')
    pickle.dump(syllables_dict, syllables_dict_file)
    syllables_dict_file.close()

    print(syllables_dict)

  print('DONE')
