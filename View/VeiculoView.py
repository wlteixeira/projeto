from flask import Flask, render_template, request, redirect
from VeiculoDao import VeiculoDao
from ClienteDao import ClienteDao
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
            idveiculo = request.form.get('idveiculo')
            idveiculo = int(idveiculo) if idveiculo else None

            idcliente = int(request.form['idcliente'])

            v = Veiculo(
                idveiculo,
                idcliente,
                request.form['marca'],
                request.form['modelo'],
                request.form['ano']
            )
            dao.salvar(v)
            return redirect('/veiculos')
        
        clientes = ClienteDao(db).listar()
        return render_template("veiculo_form.html", clientes=clientes)
    
    @app.route('/veiculo_editar/<int:id>', methods=['GET','POST'])
    def veiculo_editar(id):
        if request.method == 'POST':
            v = Veiculo(
                id,
                request.form['idcliente'],
                request.form['marca'],
                request.form['modelo'],
                request.form['ano']
            )
            dao.atualizar(v)
            return redirect('/veiculos')

        veiculo = dao.listar_por_id(id)
        clientes = ClienteDao(db).listar()
        return render_template('veiculo_form.html', veiculo=veiculo, clientes=clientes)


    @app.route('/veiculo_del/<int:id>')
    def veiculo_del(id):
        dao.deletar(id)
        return redirect('/veiculos')
    
    return redirect('/')


