import tools

def index_files(files):
    index = tools.HDict()
    for file in files:
        file_content = open(file, 'rb').read()
        text = file_content.decode('ascii', 'ignore')
        text = tools.process(text)
        index[file] = text.split()
    return index

def index_keywords(keywords):
    kwIndex = tools.HDict()
    for index, word in enumerate(keywords):
        if word in kwIndex.keys():
            kwIndex[word].append(index)
        else:
            kwIndex[word] = [index]
    return kwIndex

def index_all_keywords(index):
    total = tools.HDict()
    for file in index.keys():
        total[file] = index_keywords(index[file])
    return total

def invert_index(index):
    invIndex = tools.HDict()
    for file in index.keys():
        for word in index[file].keys():
            if word in invIndex.keys():
                if file in invIndex[word].keys():
                    invIndex[word][file].extend(index[file][word][:])
                else:
                    invIndex[word][file] = index[file][word]
            else:
                invIndex[word] = {file: index[file][word]}
    return invIndex

def build_index(files=__import__('glob').glob('corpus/**/*.txt', recursive=True)):
    import pickle
    index = invert_index(index_all_keywords(index_files(files)))
    with open('index.bin', 'wb') as file: pickle.dump(index, file)

if __name__ =='__main__':
    build_index()
