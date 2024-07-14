# Smart Inventory Management System

## Overview
A smart inventory management system that uses AI to predict stock levels and optimize inventory management.

## Installation
Clone the repository and install the required libraries:
```sh
git clone https://github.com/TharunikaAshokKumar/Smart-Inventory-Management-System.gitCtrl+Shift+X.
cd Smart-Inventory-Management-System
pip install -r requirements.txt
source venv/bin/activate
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Product A\", \"category\": \"Category 1\", \"stock\": 100, \"reorder\": 50}" http://127.0.0.1:5000/add_product
curl http://127.0.0.1:5000/inventory
