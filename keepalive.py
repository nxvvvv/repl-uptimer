from flask import Flask

app = Flask(__name__)
@app.route("/")
def keep_alive():
    return "This is so i can keep the bot running when I close the Repl"

if __name__ == "__main__":
    app.run(host='0.0.0.0')