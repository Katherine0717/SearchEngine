"""Index server init."""
import os
import pathlib
import flask

app = flask.Flask(__name__)
app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")
INDEX_PATH = pathlib.Path(__file__).resolve().parent.parent

# Load inverted index, stopwords, and pagerank into memory
import index.api  # noqa: E402  pylint: disable=wrong-import-position
index.api.load_index()
