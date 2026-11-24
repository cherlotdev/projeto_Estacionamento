
from flask import Flask, render_template, request

app = Flask(__name__)

class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo

    def preco(self):
        if self.tipo == "Carro":
            return 10
        return 5

veiculos = []

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        placa = request.form["placa"]
        tipo = request.form["tipo"]

        v = Veiculo(placa, tipo)
        veiculos.append(v)

    return render_template("index.html", veiculos=veiculos)

if __name__ == "__main__":
    app.run(debug=True)
