from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('main.html')

@app.route("/kml_sample")
def kml():
    return send_from_directory(app.static_folder, 'kml_samples.kml')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
