
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def lotoResults():
    res = requests.get("https://www.loto.com.ni/")
    return res.text, res.status_code

if __name__ == "__main__":
    app.run(debug=True, host= "0.0.0.0", port=7000)
