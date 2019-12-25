import flask
from flask import jsonify
import util

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Two sided prime!</h1><p>/api/&lt;n&rt; to check if n is two sided prime</p>"

@app.route('/api/<int:n>', methods=['GET'])
def is_two_sided_prime(n):
    return jsonify(util.isTwoSidedPrime(n))

app.run()