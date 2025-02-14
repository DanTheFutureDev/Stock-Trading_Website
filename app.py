from flask import Flask, render_template, request, redirect, url_for, flash
from .models import db, User, Stock, Transaction
from .routes import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
