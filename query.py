import tools
from functools import lru_cache

@lru_cache(maxsize=None)
def query_word(word, index):
    if word in index.keys():
        return [file for file in index[word].keys()]
    else:
        return []

def union_query(query, index):
    result = []
    for word in query.split():
        result += query_word(word, index)
    return list(set(result))

@lru_cache(maxsize=None)
def intersection_query(query, index):
    result = []
    for word in query.split():
        result.append(query_word(word, index))
    return list(set.intersection(*map(set, result)))

def phrase_query(query, index):
    intResult = set(intersection_query(query, index))
    result = []
    for file in intResult:
        temp = []
        for word in query.split():
            temp.append(index[word][file][:])
        for i in range(len(temp)):
            for ind in range(len(temp[i])):
                temp[i][ind] -= i
        if set.intersection(*map(set, temp)):
            result.append(file)
    return result
