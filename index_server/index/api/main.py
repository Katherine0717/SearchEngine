"""Index api."""
import math
import pathlib
import re
import flask
import index

INDEX_PATH = pathlib.Path(__file__).resolve().parent.parent
invertedIndex = {}
termIDF = {}
stopWord = {}
pageRank = {}


@index.app.route('/api/v1/')
def routes_list():
    """Return API resource URLs."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)


@index.app.route('/api/v1/hits/')
def hits():
    """Hits."""
    query = flask.request.args.get("q").strip().split()
    weight = 0.5
    if flask.request.args.get("w") is not None:
        weight = float(flask.request.args.get("w").strip())
    new_q = remove_stopword(query)
    if not new_q:
        context0 = {"hits": []}
        return flask.jsonify(**context0)

    score_dic = page_rank(new_q, weight)

    result = []
    for score in score_dic:
        context = {
            "docid": int(score),
            "score": score_dic[score]
        }
        result.append(context)

    result = sorted(result, key=lambda x: (-x['score'], x['docid']))
    context2 = {
            "hits": result
        }

    return flask.jsonify(**context2)


def remove_stopword(queries):
    """Remove stopword from the query."""
    new_q = {}
    for query in queries:
        query = re.sub(r'[^a-zA-Z0-9]+', '', query).lower()
        if query not in stopWord:
            if query not in new_q:
                new_q[query] = 1
            else:
                new_q[query] = new_q[query] + 1
    return new_q


def page_rank(queries, weight):
    """Calulate pagerank score."""
    query_vector = []
    for query in queries.keys():
        if query not in termIDF:
            return []
        idf = termIDF[query]
        # it cant find this word in the termIDF - cant find aaaaaaa
        query_vector.append(queries[query] * idf)

    set_list = []
    score_arr = {}
    for query in queries.keys():
        set_list.append([i[0] for i in invertedIndex[query]])
    common_doc = set.intersection(*[set(list) for list in set_list])

    for i in list(common_doc):
        doc_vector = []
        for query in queries.keys():
            tf_ = 0
            di_ = 0
            for doc in invertedIndex[query]:
                if doc[0] == i:
                    tf_ = float(doc[1])
                    di_ = float(doc[2])
            doc_vector.append(tf_ * termIDF[query])

        qd_ = sum(q * d for q, d in zip(query_vector, doc_vector))
        tfidf = qd_ / (
            math.sqrt(sum(pow(q, 2) for q in query_vector))
            * math.sqrt(di_)
         )
        score_arr[i] = weight * pageRank[i] + (1 - weight) * tfidf
    return score_arr


def load_index():
    """Load index files."""
    load_inverted()
    load_stopword()
    load_pagerank()


def load_inverted():
    """Load inverted index."""
    with open((INDEX_PATH/"inverted_index"/index.app.config["INDEX_PATH"]),
              "r", encoding="utf8") as file:
        for line in file.readlines():
            lines = line.strip().split()
            if lines[0] not in invertedIndex:
                # range: (start, stop, step)
                # seperate the word and the idf
                seq = [list(lines[idx: idx+3])
                       for idx in range(2, len(lines), 3)]
                invertedIndex[lines[0]] = seq
                termIDF[lines[0]] = float(lines[1])


def load_stopword():
    """Load stopword."""
    with open(INDEX_PATH/"stopwords.txt", "r", encoding="utf8") as file:
        for line in file.readlines():
            lines = line.strip()
            if lines not in stopWord:
                stopWord[lines] = 1


def load_pagerank():
    """Load pagerank."""
    with open(INDEX_PATH/"pagerank.out", "r", encoding="utf8") as file:
        for line in file.readlines():
            lines = line.strip().split(",")
            if lines[0] not in pageRank:
                pageRank[lines[0]] = float(lines[1])
