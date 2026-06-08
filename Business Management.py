
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json

    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products(product_name, category, price, quantity) VALUES (?, ?, ?, ?)",
        (data['product_name'], data['category'], data['price'], data['quantity'])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Product Added Successfully"}), 201


@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return jsonify(products)


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    product = cursor.fetchone()

    conn.close()

    if product:
        return jsonify(product)

    return jsonify({"message": "Product Not Found"}), 404


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json

    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE products
    SET product_name=?, category=?, price=?, quantity=?
    WHERE id=?
    """, (
        data['product_name'],
        data['category'],
        data['price'],
        data['quantity'],
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Product Updated Successfully"})


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Product Deleted Successfully"})


if __name__ == "__main__":
    app.run(debug=True)

