from flask import Flask

app = Flask(__name__)

html_code = '<html><body><a href="http://127.0.0.1:5000/soda">Hola Amigo soda sarbath</a></body></html>'

@app.route("/")
def hello():
    return html_code

@app.route("/soda")
def soda():
	return "Soda Page here"

@app.route("/otherpagehere")
def some():
	return "Some other page"

if __name__ == "__main__":
    app.run()