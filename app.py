import os
from flask import Flask, jsonify, send_file

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Essential Oversized Tee", "category": "T-Shirts", "price": 349, "badge": "BESTSELLER", "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 2, "name": "Everyday Heavy Tee", "category": "T-Shirts", "price": 399, "badge": "NEW DROP", "image": "https://images.unsplash.com/photo-1503341504253-dff4815485f1?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 3, "name": "Signature Street Hoodie", "category": "Hoodies", "price": 799, "badge": "SIGNATURE", "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 4, "name": "Urban Layer Hoodie", "category": "Hoodies", "price": 899, "badge": "PREMIUM", "image": "https://images.unsplash.com/photo-1578681994506-b8f463449011?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 5, "name": "Daily Street Cap", "category": "Caps", "price": 249, "badge": "ESSENTIAL", "image": "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?auto=format&fit=crop&w=800&q=85", "sizes": ["One size"]},
    {"id": 6, "name": "Classic Logo Tee", "category": "T-Shirts", "price": 329, "badge": "", "image": "https://images.unsplash.com/photo-1527719327859-c6ce80353573?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 7, "name": "Street Essential Hoodie", "category": "Hoodies", "price": 749, "badge": "", "image": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 8, "name": "Everyday Street Cap", "category": "Caps", "price": 229, "badge": "", "image": "https://images.unsplash.com/photo-1534215754734-18e55d13e346?auto=format&fit=crop&w=800&q=85", "sizes": ["One size"]},
    {"id": 9, "name": "Core Track Jacket", "category": "Tracksuits", "price": 699, "badge": "NEW", "image": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 10, "name": "Core Track Pants", "category": "Tracksuits", "price": 599, "badge": "NEW", "image": "https://images.unsplash.com/photo-1552902865-b72c031ac5ea?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 11, "name": "Street Cargo Shorts", "category": "Shorts", "price": 449, "badge": "COMING DROP", "image": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?auto=format&fit=crop&w=800&q=85", "sizes": ["S", "M", "L", "XL", "XXL"]},
    {"id": 12, "name": "Everyday Crew Socks", "category": "Accessories", "price": 99, "badge": "ESSENTIAL", "image": "https://images.unsplash.com/photo-1582966772680-860e372bb558?auto=format&fit=crop&w=800&q=85", "sizes": ["One size"]},
    {"id": 13, "name": "SKIPPER Everyday Tote", "category": "Accessories", "price": 199, "badge": "", "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?auto=format&fit=crop&w=800&q=85", "sizes": ["One size"]},
    {"id": 14, "name": "Urban Slide", "category": "Footwear", "price": 299, "badge": "", "image": "https://images.unsplash.com/photo-1603487742131-4160ec999306?auto=format&fit=crop&w=800&q=85", "sizes": ["UK 6", "UK 7", "UK 8", "UK 9", "UK 10", "UK 11"]}
]

@app.get("/")
def home():
    return send_file("index.html")

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "SKIPPER catalogue API"})

@app.get("/api/products")
def products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    # Local development only. Use a production WSGI server and HTTPS when deployed.
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)
