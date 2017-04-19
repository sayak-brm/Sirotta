import pickle, nltk.data
from query import *

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
query = tools.process(input())

with open('corpus.index', 'rb') as file: index = pickle.load(file)

result = {}
result[0] = phrase_query(query, index)
result[1] =intersection_query(query, index)
result[2] = union_query(query, index)

print('Phrase:', ', '.join(result[0]))
print('\nIntersection:', ', '.join(result[1]))
print('\nUnion:', ', '.join(result[2]), end='\n\n')

for file in result[0]:
    with open(file, 'rb') as f: lines = tokenizer.tokenize(f.read().decode('ascii', 'ignore'))
    for line in lines:
        if query in tools.process(line):
            print(line, end='\n\n')
            break
    
