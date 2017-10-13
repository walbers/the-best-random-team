from flask import Blueprint, request

from decorators import api_wrapper

blueprint = Blueprint("api", __name__)

@blueprint.route("/on", methods=["POST"])
@api_wrapper
def turn_on():
    """Handle request to turn on an led"""
    form = request.form
    led = form.get("led")
    print("Turn on LED #{}".format(led))
    return {"success": True}

@blueprint.route("/off", methods=["POST"])
@api_wrapper
def turn_off():
    """Handle request to turn off an led"""
    form = request.form
    led = form.get("led")
    print("Turn off LED #{}".format(led))
    return {"success": True}

@blueprint.route("/color", methods=["GET", "POST"])
@api_wrapper
def color():
    """Handle request to get/set the color of an led"""
    if request.method == "GET":
        # Get the color of an LED

        form = request.args
        led = form.get("led")
        print("LED #{}: {}".format(led, [0, 0, 0]))
        return {"success": True, "color": [0, 0, 0]}
    elif request.method == "POST":
        # Set the color

        form = request.get_json
        led = form.get("led")
        color = form.get("color")
        print("Set LED #{} to {}".format(led, color))
        return {"success": True}
    return {}
