from flask import Flask, render_template, url_for
from flask_caching import Cache

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cache = Cache(app)


@app.route("/", methods=["GET"])
@cache.cached(timeout=1)
def index():
    version = 1.0
    return render_template('index.html', version=version)
