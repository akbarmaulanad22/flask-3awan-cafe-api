from flask import Blueprint
from controllers.menu_controller import get_all_menus, create_menu, update_menu, delete_menu

web = Blueprint("web", __name__)

web.route("/menus", methods=["GET"])(get_all_menus)
web.route("/menus", methods=["POST"])(create_menu)
web.route("/menus/<int:menu_id>", methods=["PUT"])(update_menu)
web.route("/menus/<int:menu_id>", methods=["DELETE"])(delete_menu)
