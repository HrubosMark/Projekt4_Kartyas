from flask import Flask, render_template

hostIp = '127.0.0.1'
hostPort = 5001
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Főoldal")

@app.route("/kresz")
def kresz():
    with open('quiz.txt', 'r', encoding='utf-8') as f:
        lista = []
        for sor in f:
            lista.append(sor.strip().split(';'))

    lista_hossz = len(lista)
    return render_template("kartya.html", title="Quiz", lista=lista, lista_hossz=lista_hossz)

@app.route("/gym")
def gym():
    with open('quiz1.txt', 'r', encoding='utf-8') as f:
        lista = []
        for sor in f:
            lista.append(sor.strip().split(';'))

    lista_hossz = len(lista)
    return render_template("kartya.html", title="Quiz", lista=lista, lista_hossz=lista_hossz)

if __name__ == '__main__':
    app.run(host=hostIp, port=hostPort, debug=False)
    print("\n")