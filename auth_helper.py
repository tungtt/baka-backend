# auth_helper.py
import urllib.request
import json
import base64
import hmac
import hashlib
import time
import os


def base64URLEncode(data):
    # https://developers.tiki.vn/docs/backend-api/platform-api/calculate-signature
    message_bytes = data.encode()
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode()
    return base64_message.replace("=", "").replace("+", "-").replace("/", "_")

def sign(secret, payload):
    return hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()


def new_request_auth_exchange(data_dict, mode="auth_exchange"):
    # https://developers.tiki.vn/docs/backend-api/platform-api/exchange-auth-token
    # https://api.tiki.vn/tiniapp-open-api/oauth/auth/token
    # Pass the config to the container
    CLIENT_KEY = os.environ.get("CLIENT_KEY")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    AUTH_ENDPOINT = os.environ.get("AUTH_ENDPOINT")
    if mode == 'auth_refresh':
        AUTH_ENDPOINT += '/refresh'

    if not CLIENT_KEY:
        raise Exception("CLIENT_KEY missing")

    if not CLIENT_SECRET:
        raise Exception("CLIENT_SECRET missing")

    if not AUTH_ENDPOINT:
        raise Exception("AUTH_ENDPOINT missing")

    headers = {
        "Content-Type": "application/json",
    }

    data = json.dumps(data_dict, separators=(',', ':'))

    my_timestamp = str(time.time_ns() // 1_000_000 )
    payload = my_timestamp + '.' + CLIENT_KEY + '.' + data
    encodedPayload = base64URLEncode(payload)
    my_signature = sign(CLIENT_SECRET, encodedPayload)

    req = urllib.request.Request(AUTH_ENDPOINT, data.encode(), headers)
    req.add_header('X-Tiniapp-Client-Id', CLIENT_KEY)
    req.add_header('X-Tiniapp-Signature', my_signature)
    req.add_header('X-Tiniapp-Timestamp', my_timestamp)

    response = urllib.request.urlopen(req)
    res = response.read()

    return res
