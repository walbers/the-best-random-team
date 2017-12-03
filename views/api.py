from flask import Blueprint, request

from decorators import api_wrapper
import utils

blueprint = Blueprint("api", __name__)

@blueprint.route("/on", methods=["POST"])
@api_wrapper
def turn_on():
    """Handle request to turn on an led"""
    if utils.send_string("on"):
        return {"success": True}
    return {"success": False}

@blueprint.route("/off", methods=["POST"])
@api_wrapper
def turn_off():
    """Handle request to turn off an led"""
    if utils.send_string("off"):
        return {"success": True}
    return {"success": False}

@blueprint.route("/send/<string>", methods=["POST"])
@api_wrapper
def send_string(string):
    """Send a string to the arduino"""
    if utils.send_string(string):
        return {"success": True}
    return {"success": False}
