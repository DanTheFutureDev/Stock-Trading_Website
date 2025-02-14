# Stock Trading Website

This is a simple stock trading website built using Flask and MySQL with SQLAlchemy for database management. The application allows users to register, trade stocks, and view their transaction history.

## Project Structure

```
stock-trading-website
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── config.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-trading-website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Ensure you have MySQL installed and running.
   - Create a database for the application.
   - Update the database connection details in `config.py`.

## Usage

1. Run the application:
   ```
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the stock trading website.

## Features

- User registration and authentication
- Stock trading functionality
- Transaction history viewing
- Responsive design with CSS and JavaScript interactivity

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.