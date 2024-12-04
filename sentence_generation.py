import pickle
import random

def get_top_5(current, ngrams):
  result = sorted(
    ngrams.get(current, {}).items(),
    key=lambda x: x[1],
    reverse=True,
  )
  return result[:5]

def generate_3_grams_syllables(ngrams, content_length=200):
  start_token = ('ta', 'rih')
  generated_content = [start_token[0], start_token[1]]
  for i in range(content_length):
    top5 = get_top_5(tuple(generated_content[-2:]), ngrams)
    if (len(top5) == 0):
      break
    generated_content.append(random.choice([ntok[0] for ntok in top5]))
  
  return ''.join(generated_content)

def generate_2_grams_syllables(ngrams, content_length=200):
  start_token = 'ta'
  generated_content = [start_token]
  for i in range(content_length):
    top5 = get_top_5(generated_content[-1], ngrams)
    if (len(top5) == 0):
      break
    generated_content.append(random.choice([ntok[0] for ntok in top5]))

  return ''.join(generated_content)

def generate_1_grams_syllables(ngrams, content_length=200):
  generated_content = []
  for i in range(content_length):
    top5 = sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:5]
    generated_content.append(random.choice([ntok[0] for ntok in top5]))

  return ''.join(generated_content)

def generate_3_grams_chars(ngrams, content_length=200):
  start_token = ('t', 'a')
  generated_content = [start_token[0], start_token[1]]
  for i in range(content_length):
    top5 = get_top_5(tuple(generated_content[-2:]), ngrams)
    if (len(top5) == 0):
      break
    generated_content.append(random.choice([ntok[0] for ntok in top5]))
  
  return ''.join(generated_content)

def generate_2_grams_chars(ngrams, content_length=200):
  start_token = 't'
  generated_content = [start_token]
  for i in range(content_length):
    top5 = get_top_5(generated_content[-1], ngrams)
    if (len(top5) == 0):
      break
    generated_content.append(random.choice([ntok[0] for ntok in top5]))

  return ''.join(generated_content)

def generate_1_grams_chars(ngrams, content_length=200):
  generated_content = []
  for i in range(content_length):
    top5 = sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:5]
    generated_content.append(random.choice([ntok[0] for ntok in top5]))

  return ''.join(generated_content)
