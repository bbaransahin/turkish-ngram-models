import re
import string

def remove_html_tags(text):
    """Remove HTML tags from the text."""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_punctuation(text):
    """Remove punctuation from the text."""
    return text.translate(str.maketrans('', '', string.punctuation))
