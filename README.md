# .-Business-Management-System_-API
#  Business Management System API

A RESTful API built using Flask and SQLite for managing business products. This project allows users to add, view, update, and delete products efficiently.

##  Features

- Add Products
- View Products
- Update Product Details
- Delete Products
- SQLite Database Integration
- REST API Architecture

##  Used

- Python
- Flask
- SQLite3
- REST API

##  Project Structure

business-management-system/
│
├── app.py
├── business.db
├── README.md
└── requirements.txt

##  Installation


```bash
pip install flask
```

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

##  API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /products | Add Product |
| GET | /products | Get All Products |
| GET | /products/<id> | Get Product |
| PUT | /products/<id> | Update Product |
| DELETE | /products/<id> | Delete Product |

## Example Request

```json
{
  "product_name": "Laptop",
  "category": "Electronics",
  "price": 75000,
  "quantity": 10
}
```


## Author

Maheen Asad
## LINK
https://github.com/m9544998/.-Business-Management-System_-API
```
THANKYOU
```
