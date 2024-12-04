import math
import syllables
import generate_text

def get_total_grams(data, n):
  c = 0
  if (n == 1): # for 1 grams
    c = sum(data.values())
  else: # for 2 or 3 grams
    for gram in data.values():
      c += sum(gram.values())
  return c

def get_frequencies(data, n):
  frequencies = {}
  if (n == 1): # for 1 grams
    for freq in data.values():
      if (freq not in frequencies):
        frequencies[freq] = 0
      frequencies[freq] += 1
  else: # for 2 or 3 grams
    for sub_dict in data.values():
      for freq in sub_dict.values():
        if (freq not in frequencies):
          frequencies[freq] = 0
        frequencies[freq] += 1
  return frequencies

def get_good_turing_count(count, frequencies):
  if (count+1 in frequencies and count in frequencies):
    return (count+1)*(frequencies[count+1]/frequencies[count])
  elif count in frequencies:
    return count
  return 1e-6

def get_probability(k, w, data, frequencies):
  if (k in data and w in data[k]):
    good_turing_count = get_good_turing_count(data[k][w], frequencies)
  else:
    good_turing_count = get_good_turing_count(0, frequencies)
  return good_turing_count/total_grams

def get_probability_1_grams(ch, data, frequencies):
  if ch in data:
    good_turing_count = get_good_turing_count(data[ch], frequencies)
  else:
    good_turing_count = get_good_turing_count(0, frequencies)
  return good_turing_count / total_grams

def get_perplexity(train_data, test_data, n):
  test_corpus = syllables.syllabicate(test_data)
  test_syllables = []
  for word in test_corpus:
    for i in range(len(word)):
      if (i == len(word)-1):
        test_syllables.append(word[i]+' ')
      else:
        test_syllables.append(word[i])

  print(test_syllables[:100])

  log_sum = 0
  if (n == 1): # for 1 grams
    for i in test_syllables:
      prob = get_probability_1_grams(
        i,
        train_data,
        frequencies,
      )
      log_sum += math.log(prob)

    avg_log = log_sum/len(test_syllables)
    p = math.exp(-avg_log)

  elif (n == 2): # for 2 grams
    for i in range(len(test_syllables)-1):
      prob = get_probability(
        test_syllables[i],
        test_syllables[i+1],
        train_data,
        frequencies,
      )
      log_sum += math.log(prob)
    avg_log = log_sum/(len(test_syllables)-1)
    p = math.exp(-avg_log)

  elif (n == 3): # for 3 grams
    for i in range(len(test_syllables)-2):
      prob = get_probability(
        tuple(test_syllables[i:i+2]),
        test_syllables[i+2],
        train_data,
        frequencies,
      )
      log_sum += math.log(prob)
    avg_log = log_sum/(len(test_syllables)-2)
    p = math.exp(-avg_log)
  return p

import pickle
fi = open('syllables_dict_3_grams.pkl', 'rb')
data = pickle.load(fi)
fi.close()

for key in data:
  print (key)
  break

fi = open('preprocessed_test', 'r')
test_data = fi.read()
fi.close()

total_grams = get_total_grams(data, 3)
frequencies = get_frequencies(data, 3)

p = get_perplexity(data, test_data, 3)
print(p)
