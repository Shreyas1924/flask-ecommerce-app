# Flask E-Commerce Web Application

A full-stack **E-Commerce web application** built using **Python Flask, SQLite, and SQLAlchemy**.
This project demonstrates core backend development concepts including **database integration, session-based cart management, user authentication, and order processing**.

---

## Author

**Shreyas S D**

---

## Project Overview

This project implements the basic functionality of an online shopping platform. Users can browse products, add items to a shopping cart, manage product quantities, checkout, and view order history. The application also includes a simple admin feature to add products.

The goal of this project is to demonstrate how a backend-driven web application works using **Flask and relational databases**.

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
* Session-based cart management

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

## Application Workflow

Products → Cart → Checkout → Order stored in database → Order history

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Shreyas1924/flask-ecommerce-app.git
```

Navigate to the project folder:

```bash
cd flask-ecommerce-app
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```

---

## Project Structure

```
flask-ecommerce-app
│
├── app.py                 # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignored files
│
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── products.html
│   ├── cart.html
│   ├── login.html
│   ├── register.html
│   ├── add_product.html
│   ├── orders.html
│   └── checkout_success.html
│
└── instance/
    └── store.db           # SQLite database
```

---

## Future Improvements

Planned improvements for the project include:

* Product images
* Product search functionality
* Admin product edit and delete features
* Payment gateway integration
* Improved UI design
* Order tracking system

---

## License

This project is created for **educational and learning purposes**.
