import re
from nltk.corpus import wordnet
from textblob import Word

def process(string):
    stopwords = [word[:-1].lower() for word in open('stopwords.txt', 'r')]
    pattern = re.compile('[\W_]+')
    string = pattern.sub(' ', string).lower()
    words = string.split()
    resultwords  = [Word(word).lemmatize(pos=wordnet.VERB) for word in words if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    return result

class HDict(dict):
    def __hash__(self):
        return hash(frozenset(self.keys()))
