from hello import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hllo, World!<p>"