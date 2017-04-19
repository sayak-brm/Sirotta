import re, bs4
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

def filter_html(string):
    soup = bs4.BeautifulSoup(string, 'html.parser')
    elements = soup.strings
    def visible(element):
        if element.parent.name in ['meta', 'style', 'script', '[document]', 'head', 'title']:
            return False
        elif isinstance(element, bs4.element.Comment):
            return False
        return True
    return ' '.join([element for element in elements if visible(element)])
