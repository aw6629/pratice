from flask import Flask, render_template,jsonify

app = Flask(__name__)

@app.route("/")

def default_page():

    return jsonify({'id':1,'name':'AA'})


if __name__ == "__main__":

    app.run(debug=True, use_reloader=True)