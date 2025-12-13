from flask import Flask, render_template, request, redirect
from ClienteDao import ClienteDao
from Model.Cliente import Cliente


def init_cliente_routes(app, db):
    dao = ClienteDao(db)


    @app.route('/clientes')
    def clientes():
        lista = dao.listar()
        return render_template("cliente_listar.html", lista=lista)


    @app.route('/cliente_novo', methods=["GET", "POST"])
    def cliente_novo():
        if request.method == "POST":
            id = request.form.get('idcliente')  

            if id:
                id = int(id)
            else:
                id = None

            cliente = Cliente(
                idcliente=id,
                nome=request.form.get('nome'),
                endereco=request.form.get('endereco'),
                telefone=request.form.get('telefone')
            )

            dao.salvar(cliente)
            return redirect('/clientes')

        return render_template("cliente_form.html")


    @app.route('/cliente_del/<int:id>')
    def cliente_del(id):
        dao.deletar(id)
        return redirect('/clientes')

    return redirect('/')
