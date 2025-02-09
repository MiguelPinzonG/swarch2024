from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.products_service import ProductService

product_blueprint = Blueprint('products', __name__)

@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.form
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    ProductService.create_product(name, description)
    return redirect(url_for('products.index'))

@product_blueprint.route('/products/update', methods=['POST'])
def update_product():
    data = request.form
    product_id = data.get('product_id')
    new_name = data.get('new_name')
    new_description = data.get('new_description')
    if not product_id or not new_name:
        return jsonify({'error': 'Product ID and new name are required'}), 400
    updated_product = ProductService.update_product(product_id, new_name, new_description)
    if updated_product:
        return jsonify({'message': 'Product updated successfully'}), 200
    return jsonify({'error': 'Product not found'}), 404

@product_blueprint.route('/')
def index():
    return render_template('index.html')