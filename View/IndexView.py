from flask import Flask, render_template, request, redirect


def init_index_routes(app, db):

    @app.route('/')
    def index():
        return render_template("index.html")