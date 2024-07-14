# Smart Inventory Management System

## Overview
A smart inventory management system that uses AI to predict stock levels and optimize inventory management.

## Installation

### Prerequisites
- Python 3.x
- Git

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/TharunikaAshokKumar/Smart-Inventory-Management-System.git
    cd Smart-Inventory-Management-System
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python src/inventory.py
    ```

## Usage

1. Set environment variables:
    ```sh
    set FLASK_APP=src/main.py
    set FLASK_ENV=development
    ```

2. Run the Flask application:
    ```sh
    flask run
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Testing Endpoints

### Add a Product
```sh
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Product A\", \"category\": \"Category 1\", \"stock\": 100, \"reorder\": 50}" http://127.0.0.1:5000/add_product
