from flask import Flask, render_template

import views

app = Flask(__name__)

app.register_blueprint(views.api.blueprint, url_prefix="/api/led")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
