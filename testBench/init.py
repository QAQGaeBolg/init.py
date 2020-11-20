from flask import Flask
from flask import request
from flask import send_file
import kernel

app = Flask(__name__)
app.debug = True


@app.route("/")
def test_controller():
    return send_file("static/test.html")


@app.route("/test/api/dialog_analyze", methods=['Post'])
def dialog_analyze():
    string = request.data
    string = kernel.__kernel__(string[2:len(string)-1])
    return string


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
