from flask import Flask, render_template, request, redirect
from OrdemServicoDao import OrdemServicoDao
from Model.OrdemServico import OrdemServico


def init_os_routes(app,db):
    dao = OrdemServicoDao(db)

    @app.route('/os')
    def os_listar():
        lista = dao.listar()
        return render_template("os_listar.html", lista=lista)


    @app.route('/os_nova', methods=["GET", "POST"])
    def os_nova():
        if request.method == "POST":
            o = OrdemServico(
                request.form['idordemservico'],
                request.form['idveiculo'],
                request.form['prazo'],
                request.form['defeito'],
                request.form['valortotal']
            )
            dao.salvar(o)
            return redirect('/os')

        return render_template("os_form.html")


    @app.route('/os_del/<int:id>')
    def os_del(id):
        dao.deletar(id)
        return redirect('/os')

    return redirect('/')