from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from View.VeiculoView import init_veiculo_routes
from View.ClienteView import init_cliente_routes
from View.OrdemServiçoView import init_os_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = 'barro'
    app.config.from_pyfile('config.py')
    db = MySQL(app)

    init_cliente_routes(app, db)
    init_os_routes(app, db)
    init_veiculo_routes(app, db)
    return app, db

if __name__ == '__main__':
    app, db = create_app()
    app.run(debug=True)
