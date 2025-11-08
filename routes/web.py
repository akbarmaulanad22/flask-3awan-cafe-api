from flask import Blueprint
from controllers.menu_controller import get_all_menus, create_menu, update_menu, delete_menu
from controllers.order_controller import create_order, get_all_orders, get_order_by_id

web = Blueprint("web", __name__)

web.route("/menus", methods=["GET"])(get_all_menus)
web.route("/menus", methods=["POST"])(create_menu)
web.route("/menus/<int:menu_id>", methods=["PUT"])(update_menu)
web.route("/menus/<int:menu_id>", methods=["DELETE"])(delete_menu)

web.route("/orders", methods=["GET"])(get_all_orders)
web.route("/orders/<int:order_id>", methods=["GET"])(get_order_by_id)
web.route("/orders", methods=["POST"])(create_order)
