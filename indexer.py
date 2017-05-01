import tools
import pickle, tempfile, shutil

def index_files(files):
    for file in files:
        print(file)
        file_content = open(file, 'rb').read()
        text = file_content.decode('ascii', 'ignore')
        text = tools.process(tools.filter_html(text))
        with open('{}/{}.index'.format(temp, tools.process(file)), 'wb') as dump: pickle.dump(index_keywords(text.split()), dump)

def index_keywords(keywords):
    kwIndex = tools.HDict()
    for index, word in enumerate(keywords):
        if word in kwIndex.keys():
            kwIndex[word].append(index)
        else:
            kwIndex[word] = [index]
    return kwIndex
        
def invert_index(files):
    invIndex = tools.HDict()
    for file in files:
        print(file)
        with open('{}/{}.index'.format(temp, tools.process(file)), 'rb') as dump: index = pickle.load(dump)
        for word in index.keys():
            if word in invIndex.keys():
                if file in invIndex[word].keys():
                    invIndex[word][file].extend(index[word][:])
                else:
                    invIndex[word][file] = index[word]
            else:
                invIndex[word] = {file: index[word]}
    return invIndex

def build_index(files=__import__('glob').glob('corpus/**/*.html', recursive=True)):
    print('Stage 1:\n')
    index_files(files)
    input('\n\nStage 2:\n')
    with open('corpus.index', 'wb') as file: pickle.dump(invert_index(files), file)

if __name__ =='__main__':
    global temp
    temp = tempfile.mkdtemp()
    build_index()
    shutil.rmtree(temp)
