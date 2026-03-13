# Flask E-Commerce Web Application

## Author

Shreyas S D

## Project Overview

This project is a full-stack E-Commerce web application built using Python Flask and SQLite.
The system allows users to browse products, add items to a cart, manage quantities, place orders, and view order history.

The application demonstrates backend web development concepts including database integration, session management, and user authentication.

---

## Features

### User Features

* Browse available products
* Add products to cart
* Increase or decrease product quantity
* Remove items from cart
* Checkout and place orders
* View order history
* User registration
* User login and logout

### Admin Features

* Add products directly from the admin page

---

## Technologies Used

### Backend

* Python
* Flask

### Database

* SQLite
* SQLAlchemy ORM

### Frontend

* HTML
* Bootstrap

---

## Project Workflow

Products → Cart → Checkout → Order stored in database → Order history

---

## Installation

Clone the repository:

git clone https://github.com/Shreyas1924/flask-ecommerce-app.git

Navigate to the project folder:

cd flask-ecommerce-app

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open the application in your browser:

http://127.0.0.1:5000

---

## Future Improvements

* Product images
* Product search
* Admin edit/delete products
* Payment gateway integration
* Better UI design

---

## Project Structure

app.py – Main Flask application
models.py – Database models
templates/ – HTML templates
requirements.txt – Project dependencies
.gitignore – Files ignored by Git

---

## License

This project is for educational and learning purposes.
