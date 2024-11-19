import requests
from requests.auth import HTTPBasicAuth
import json
from tweeter.models import Token

from tweeter.tweet import (
    client_secret,
    client_id,
)


def refresh_token():
    t = Token.objects.get(name="token")
    data = json.loads(t.token.replace("'", '"'))
    refresh_t = data["refresh_token"]
    token_url = "https://api.x.com/2/oauth2/token"

    auth = HTTPBasicAuth(client_id, client_secret)

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_t
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(token_url, data=data, headers=headers, auth=auth)

    if response.status_code == 200:
        refreshed_token = response.json()
        return refreshed_token
    else:
        print("Error ", response.json().get("error_description"))
        return None
