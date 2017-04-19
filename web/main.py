import cgi, pickle, template
from query import *

def main():
    template.html_top(title="Sirotta")
    form = cgi.FieldStorage()
    if 'q' not in form:
        print('<h2>Error: Empty Query</h2>')
        template.html_bottom()
        return
    query = tools.process(form['q'].value)
    with open('corpus.index', 'rb') as file: index = pickle.load(file)
    print('<h3>Searching for:</h3><h4>', query, '</h4>')
    result = {}
    result[0] = phrase_query(query, index)
    result[1] =intersection_query(query, index)
    result[2] = union_query(query, index)
    results = result[0][:]
    results.extend(x for x in result[1] if x not in results)
    results.extend(x for x in result[2] if x not in results)
    print('<p>', '</p><p>'.join(results), '</p>')
    template.html_bottom()

main()
