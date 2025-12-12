from flask import Flask, render_template, request, redirect
from VeiculoDao import VeiculoDao
from Model.Veiculo import Veiculo

def init_veiculo_routes(app, db):
    dao = VeiculoDao(db)

    @app.route('/veiculos')
    def veiculos():
        lista = dao.listar()
        return render_template("veiculo_listar.html", lista=lista)


    @app.route('/veiculo_novo', methods=["GET", "POST"])
    def veiculo_novo():
        if request.method == "POST":
            v = Veiculo(
                request.form['idveiculo'],
                request.form['idcliente'],
                request.form['marca'],
                request.form['modelo'],
                request.form['ano']
            )
            dao.salvar(v)
            return redirect('/veiculos')

        return render_template("veiculo_form.html")


    @app.route('/veiculo_del/<int:id>')
    def veiculo_del(id):
        dao.deletar(id)
        return redirect('/veiculos')
    
    return redirect('/')


