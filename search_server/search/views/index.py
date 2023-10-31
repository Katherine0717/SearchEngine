"""Renders index."""
import heapq
import threading
import requests
import flask
import search


def request(url, parameters, results):
    """Get results from url."""
    req = requests.get(url, params=parameters, timeout=5)
    results.append(req.json()["hits"])


@search.app.route('/', methods=["GET"])
def show_index():
    """Get results from inverted_index."""
    weight = 0.5
    if 'w' in flask.request.args:
        weight = flask.request.args.get('w', type=float)
    if 'q' not in flask.request.args:
        context = {"slider": weight, "display": ""}
        return flask.render_template("index.html", **context)
    query = flask.request.args.get('q')
    if not query:
        context = {"slider": weight, "display": ""}
        return flask.render_template("index.html", **context)

    w_q = {'w': weight, 'q': query}
    results = []
    threads = []

    for url in search.app.config['SEARCH_INDEX_SEGMENT_API_URLS']:
        thread = threading.Thread(target=request, args=(url, w_q, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    hits = heapq.merge(*results, reverse=True, key=lambda s: s["score"])
    docs = []

    connection = search.model.get_db()
    count = 0
    for hit in hits:
        cur = connection.execute(
            "SELECT * "
            "FROM Documents "
            "WHERE docid == ? ", (hit['docid'], )
        )
        docs.append(cur.fetchone())
        count += 1
        if count == 10:
            break

    context = {"slider": weight, "display": query, "docs": docs}
    return flask.render_template("index.html", **context)
