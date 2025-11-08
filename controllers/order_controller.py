from flask import request, jsonify
from config.database import get_db
from models.order_model import Order, OrderItem
from models.menu_model import Menu

def create_order():
    data = request.json
    db = next(get_db())

    items_data = data.get("items", [])

    if not items_data:
        return jsonify({"message": "Items are required"}), 400

    total_price = 0
    order_items = []
    for item in items_data:
        menu = db.query(Menu).filter(Menu.id == item["menuId"]).first()
        if not menu:
            return jsonify({"message": f"Menu with id {item['menuId']} not found"}), 404

        qty = item.get("quantity", 1)
        total_price += menu.price * qty

        order_items.append(OrderItem(
            menu_id=menu.id,
            quantity=qty,
            price=menu.price
        ))

    new_order = Order(
        total_price=total_price,
        items=order_items
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return jsonify(new_order.to_dict()), 201


def get_all_orders():
    db = next(get_db())
    orders = db.query(Order).all()
    return jsonify([o.to_dict() for o in orders])


def get_order_by_id(order_id):
    db = next(get_db())
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return jsonify({"message": "Order not found"}), 404
    return jsonify(order.to_dict())
