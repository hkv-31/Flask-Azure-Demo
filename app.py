from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Running Hetanshi's app on azure"

if __name__ == "__main__":
    app.run()
