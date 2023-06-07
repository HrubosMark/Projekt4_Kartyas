from flask import Flask, render_template, url_for

hostIp = '127.0.0.1'
hostPort = 5001
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Főoldal")

@app.route("/kartya")
def kartya():
    lista = [["asd", "asddf"],["cihjga", "a"]]

    return render_template("kartya.html", title="Quiz", lista=lista)

if __name__ == '__main__':
    app.run(host=hostIp, port=hostPort, debug=False)
    print("\n")