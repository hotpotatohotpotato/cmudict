import os

from flask import Flask, render_template, request

from cmudict_loader import CMUDict


app = Flask(__name__)

DICT_PATH = os.path.join(os.path.dirname(__file__), "cmudict.dict")
CMU = CMUDict(dict_path=DICT_PATH)


@app.route("/", methods=["GET"])
def index():
    query = request.args.get("q", "").strip()
    results = CMU.lookup(query) if query else None
    return render_template(
        "index.html",
        query=query,
        results=results,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
