from flask import Flask, render_template, request, redirect
from OrdemServicoDao import OrdemServicoDao
from Model.OrdemServico import OrdemServico
from VeiculoDao import VeiculoDao

def init_os_routes(app,db):
    dao = OrdemServicoDao(db)

    @app.route('/os')
    def os_listar():
        lista = dao.listar()
        return render_template("os_listar.html", lista=lista)


    @app.route('/os_nova', methods=["GET", "POST"])
    def os_nova():
        if request.method == "POST":
            idordemservico = request.form.get('idordemservico')  

            if idordemservico:
                idordemservico = int(idordemservico)
            else:
                idordemservico = None

            idveiculo = int(request.form['idveiculo'])
            prazo = request.form['prazo']
            defeito = request.form['defeito']
            valortotal = request.form['valortotal']

            o = OrdemServico(
                idordemservico,
                idveiculo,
                prazo,
                defeito,
                valortotal
            )
            dao.salvar(o)
            return redirect('/os')
        veiculos= VeiculoDao(db).listar()
        return render_template("os_form.html", veiculos=veiculos)
    
    @app.route('/os_editar/<int:id>', methods=['GET','POST'])
    def os_editar(id):
        if request.method == 'POST':
            os = OrdemServico(
                id,
                request.form['idveiculo'],
                request.form['prazo'],
                request.form['defeito'],
                request.form['valortotal']
            )
            dao.atualizar(os)
            return redirect('/os')

        os = dao.listar_por_id(id)
        veiculos = VeiculoDao(db).listar()
        return render_template('os_form.html', os=os, veiculos=veiculos)

    @app.route('/os_del/<int:id>')
    def os_del(id):
        dao.deletar(id)
        return redirect('/os')

    return redirect('/')