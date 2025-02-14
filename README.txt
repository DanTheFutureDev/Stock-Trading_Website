
Stock Trading Website

This project is a stock trading website built using Flask, SQLAlchemy, and Alembic for database migrations. Below is an overview of the main functions and how the code works.

1. Application Structure
-------------------------
- app/
  - __init__.py: Initializes the Flask application, sets up the database, and registers blueprints.
  - models.py: Defines the database models for User, Stock, and Transaction.
  - routes.py: Contains the route handlers for the application.
  - templates/
    - register.html: The registration page template.
- migrations/: Contains database migration scripts.
- config.py: Configuration file for the Flask application.
- requirements.txt: Lists the dependencies required for the project.

2. Configuration
----------------
The configuration for the Flask application is defined in config.py. It includes settings for the secret key, database URI, and SQLAlchemy options.

3. Database Models
------------------
The database models are defined in models.py:
- User: Represents a user in the system with attributes such as username, email, password, balance, and transactions.
- Stock: Represents a stock with attributes such as symbol, name, price, and transactions.
- Transaction: Represents a transaction with attributes such as user_id, stock_id, quantity, transaction_type, and timestamp.

4. Routes
---------
The routes are defined in routes.py:
- /: Renders the index.html template.
- /register: Handles user registration. Validates the form data, checks for existing users, and adds new users to the database.
- /trade: Handles stock trading. Displays the trade form and processes trade requests.
- /transactions: Displays the user's transactions.
- /buy: Handles buying stocks. Checks for sufficient funds and records the transaction.
- /sell: Handles selling stocks. Records the transaction.
- /test_db: Tests the database connection and returns the user count.

5. Database Migrations
----------------------
Database migrations are managed using Alembic. The migration scripts are located in the migrations/versions/ directory. The add_balance_to_user.py script adds the balance column to the user table.

6. Running the Application
--------------------------
To run the application, follow these steps:
1. Activate the virtual environment:
   - Windows: venv\Scripts\activate
   - macOS/Linux: source venv/bin/activate
2. Install the dependencies:
   pip install -r requirements.txt
3. Apply the database migrations:
   flask db upgrade
4. Start the Flask application:
   flask run

7. Logging
----------
Logging is configured in __init__.py. SQLAlchemy logging is enabled to capture SQL statements being executed.

This README provides an overview of the main functions and how the code works. For more detailed information, refer to the individual files and their comments.
