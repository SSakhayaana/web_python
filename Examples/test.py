from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/page_two")
def page_two():
    return "<h1 style='color: #cc00cc;'>Two page</h1>"

# точка входа
if __name__ == "__main__":
    app.run(debug=True)