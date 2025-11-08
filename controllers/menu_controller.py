from flask import request, jsonify
from config.database import get_db
from models.menu_model import Menu

def get_all_menus():
    db = next(get_db())
    menus = db.query(Menu).all()
    return jsonify([m.to_dict() for m in menus])


def create_menu():
    data = request.json
    db = next(get_db())

    new_menu = Menu(
        title=data["title"],
        image_path=data["imagePath"],
        price=data["price"],
        category=data["category"],  # ✅ Required
        is_best_seller=data.get("isBestSeller", False),
    )

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return jsonify(new_menu.to_dict()), 201


def update_menu(menu_id):
    db = next(get_db())
    menu = db.query(Menu).filter(Menu.id == menu_id).first()

    if not menu:
        return jsonify({"message": "Menu not found"}), 404

    data = request.json
    menu.title = data.get("title", menu.title)
    menu.image_path = data.get("imagePath", menu.image_path)
    menu.price = data.get("price", menu.price)
    menu.category = data.get("category", menu.category)  # ✅ Bisa update
    menu.is_best_seller = data.get("isBestSeller", menu.is_best_seller)

    db.commit()
    db.refresh(menu)

    return jsonify(menu.to_dict())


def delete_menu(menu_id):
    db = next(get_db())
    menu = db.query(Menu).filter(Menu.id == menu_id).first()

    if not menu:
        return jsonify({"message": "Menu not found"}), 404

    db.delete(menu)
    db.commit()

    return jsonify({"message": "Menu deleted successfully"})
