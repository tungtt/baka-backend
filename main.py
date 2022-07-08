# main.py
import os
from flask import Flask, request

import auth_helper

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Baka - Creative Content meets Blockchain!"


@app.route("/api/v1/auth_exchange", methods=["POST"])
def auth_exchange_handler():
    # curl -X 'POST'
    #      -d '{"code": ""}'
    #      -H 'Content-Type: application/json'
    #      -H 'X-Tiniapp-Client-Id: '
    #      -H 'X-Tiniapp-Signature: '
    #      -H 'X-Tiniapp-Timestamp: '
    # 'https://api.tiki.vn/tiniapp-open-api/oauth/auth/token'
    data_dict = request.get_json()

    if not data_dict:
        msg = "No payload received"
        app.logger.error(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(data_dict, dict):
        msg = "Invalid payload data format"
        app.logger.error(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not "code" in data_dict:
        msg = "Missing key 'code'"
        app.logger.error(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    try:
        # {
        #   "data":{
        #     "access_token": "",
        #     "expires_in": 3600,
        #     "refresh_token": "",
        #     "scopes":[
        #       "offline",
        #       "user_profile"
        #     ],
        #     "token_type": "bearer",
        #     "customer": {
        #       "id": 1,
        #       "name": "Ti Ni",
        #     }
        #   },
        #   "error": null
        # }
        output = auth_helper.new_request_auth_exchange(data_dict)
        return output, 200
    except Exception as err:
        return f"Error: {err}", 500

@app.route("/api/v1/auth_refresh", methods=["POST"])
def auth_refresh_handler():
    # curl -X 'POST' -d '{"refresh_token": ""}'
    #      -H 'Content-Type: application/json'
    #      -H 'X-Tiniapp-Client-Id: '
    #      -H 'X-Tiniapp-Signature: '
    #      -H 'X-Tiniapp-Timestamp: '
    # 'https://api.tiki.vn/tiniapp-open-api/oauth/auth/token/refresh'
    data_dict = request.get_json()

    if not data_dict:
        msg = "No payload received"
        app.logger.error(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(data_dict, dict):
        msg = "Invalid payload data format"
        app.logger.error(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not "refresh_token" in data_dict:
        msg = "Missing key 'refresh_token'"
        app.logger.error(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    try:
        # {
        #   "data":{
        #     "access_token": "",
        #     "expires_in": 3600,
        #     "refresh_token": "",
        #     "scopes":[
        #       "offline",
        #       "user_profile"
        #     ],
        #     "token_type": "bearer"
        #   },
        #   "error": null
        # }
        output = auth_helper.new_request_auth_exchange(data_dict, mode='auth_refresh')
        return output, 200
    except Exception as err:
        return f"Error: {err}", 500


if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080
    app.run(host="0.0.0.0", port=PORT, debug=True)
