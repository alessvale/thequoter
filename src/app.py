
from flask import Flask, render_template, jsonify, request
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

####Quote generation
###Obtained from https://silgro.com/fortunes.htm#section_p
# with open("raw.txt", "r") as f:
#     text = f.readlines()
# quotes = []
# authors = []
# for q in text:
#     parts = q.split("â€")
#     if len(parts) == 2:
#         quotes.append(parts[0].strip())
#         authors.append(parts[1].strip("” "))
#
# quotes_clean = []
# for q in quotes:
#     if q[0] == '"':
#         q = q[1:]
#     if q[-1] == '"':
#         q =q[:-1]
#     quotes_clean.append(q)
#
# with open("corpus.txt", "w") as f:
#     for p in quotes_clean:
#         f.writelines(p + "\n")
# with open("authors.txt", "w") as f:
#     for p in authors:
#         f.writelines(p)
####
def similCompute(X, y):
    simil = []
    for i in range(X.shape[0]):
        row = X[i, :]
        if np.linalg.norm(y) == 0:
            return np.random.randint(X.shape[0])
        sim = np.dot(row, y.T)/(np.linalg.norm(row) * np.linalg.norm(y))
        simil.append(sim)
    return np.argmax(simil)

with open("corpus.txt", "r") as f:
        corpus = [s.strip() for s in f.readlines()]
with open("authors.txt", "r") as f:
        authors= [s.strip() for s in f.readlines()]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus).todense()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/compute', methods=['POST'])
def parse_text():
    text = request.form.get("text")
    if len(text) > 0:
        y = vectorizer.transform([text]).todense()
        idx = similCompute(X, y)
        quote = corpus[idx]
        auth = authors[idx]
    else:
        quote = ""
        auth = ""
    obj = [{"quote": [quote, auth]}]
    return jsonify(obj)

port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = port)
    #app.run(debug = True)
