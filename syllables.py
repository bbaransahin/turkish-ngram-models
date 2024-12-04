from turkishnlp import detector
from tqdm import tqdm

def chunk_text(text, chunk_size):
  words = text.split()
  for i in range(0, len(words), chunk_size):
    yield ' '.join(words[i:i + chunk_size])

def syllabicate(text):
  syllables_dict = {}
  obj = detector.TurkishNLP()
  syllables = obj.syllabicate_sentence(text)
  return syllables


'''
def syllabicate(text, chunk_size):
  syllables_dict = {}
  obj = detector.TurkishNLP()
  for chunk in tqdm(chunk_text(text, chunk_size)):
    syllables = obj.syllabicate_sentence(chunk)
    for s in syllables_dict:
      if (s in syllables_dict):
        syllables_dict[s] += 1
      else:
        syllables_dict[s] = 1
  return syllables_dict

for i in syllabicate('bu bir cumle ve bu cumlenin nasil bolundugunu gormek istiyorum', 2):
  print(i)
'''
