from blog import app


@app.route("/")
def homepage():
    return "<h1>Homepage</h1>"