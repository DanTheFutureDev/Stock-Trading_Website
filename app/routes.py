from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import logging
from .models import db, User, Stock, Transaction

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        return render_template('index.html', user=user)
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            logging.info(f"Attempting to register user: {username}")
            
            if not username or not password or not email:
                logging.warning("Username, email, or password not provided.")
                flash('Username, email, and password are required.', 'danger')
                return redirect(url_for('main.register'))
            
            # Check if the username already exists
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                logging.warning(f"Username {username} already exists.")
                flash('Username already exists.', 'danger')
                return redirect(url_for('main.register'))
            
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            logging.info(f"User {username} registered successfully.")
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('main.index'))
    except Exception as e:
        logging.error(f"Error during registration: {e}")
        flash('An error occurred during registration.', 'danger')
        db.session.rollback()  # Rollback the session in case of error
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))

@main.route('/trade', methods=['GET', 'POST'])
def trade():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        quantity = request.form['quantity']
        # Logic for trading stocks would go here
        flash(f'Trade executed for {quantity} shares of {stock_symbol}.', 'success')
        return redirect(url_for('main.index'))
    return render_template('trade.html')

@main.route('/transactions')
def transactions():
    user_transactions = Transaction.query.all()  # Fetch user's transactions
    return render_template('transactions.html', transactions=user_transactions)

@main.route('/buy', methods=['POST'])
def buy_stock():
    try:
        if 'user_id' not in session:
            flash('You need to log in first.', 'danger')
            return redirect(url_for('main.index'))
        
        symbol = request.form['symbol']
        quantity = int(request.form['quantity'])
        stock = Stock.query.filter_by(symbol=symbol).first()
        
        if not stock:
            flash('Stock not found.', 'danger')
            return redirect(url_for('main.index'))
        
        user_id = session['user_id']
        user = User.query.get(user_id)
        
        # Check if user has enough funds (assuming user has a 'balance' attribute)
        total_cost = stock.price * quantity
        if user.balance < total_cost:
            flash('Insufficient funds.', 'danger')
            return redirect(url_for('main.index'))
        
        transaction = Transaction(user_id=user_id, stock_id=stock.id, quantity=quantity, transaction_type='buy')
        user.balance -= total_cost
        db.session.add(transaction)
        db.session.commit()
        
        flash(f'Successfully bought {quantity} shares of {symbol}.', 'success')
    except Exception as e:
        logging.error(f"Error buying stock: {e}")
        flash('An error occurred while processing your request.', 'danger')
    
    return redirect(url_for('main.index'))

@main.route('/sell', methods=['POST'])
def sell_stock():
    try:
        if 'user_id' not in session:
            flash('You need to log in first.', 'danger')
            return redirect(url_for('main.index'))
        
        symbol = request.form['symbol']
        quantity = int(request.form['quantity'])
        stock = Stock.query.filter_by(symbol=symbol).first()
        
        if not stock:
            flash('Stock not found.', 'danger')
            return redirect(url_for('main.index'))
        
        user_id = session['user_id']
        user = User.query.get(user_id)
        
        transaction = Transaction(user_id=user_id, stock_id=stock.id, quantity=quantity, transaction_type='sell')
        db.session.add(transaction)
        db.session.commit()
        
        flash(f'Successfully sold {quantity} shares of {symbol}.', 'success')
    except Exception as e:
        logging.error(f"Error selling stock: {e}")
        flash('An error occurred while processing your request.', 'danger')
    
    return redirect(url_for('main.index'))

@main.route('/test_db')
def test_db():
    try:
        # Attempt to query the database
        user_count = User.query.count()
        return f"Database connected successfully. User count: {user_count}"
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        return "Database connection failed."