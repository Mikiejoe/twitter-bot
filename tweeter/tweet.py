import base64
import hashlib
import os
import re
import requests
from decouple import config

# from requests.auth import AuthBase, HTTPBasicAuth
from requests_oauthlib import OAuth2Session  # , TokenUpdated

client_id = config("CLIENT_ID")
client_secret = config("CLIENT_SECRET")
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url = "https://api.x.com/2/oauth2/token"
scopes = ["tweet.read", "users.read", "tweet.write", "offline.access"]
code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)
code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
code_challenge = code_challenge.replace("=", "")
redirect_uri = config("REDIRECT_URI")


def make_token():
    return OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)


def post_tweet(payload, token):
    return requests.request(
        "POST",
        "https://api.x.com/2/tweets",
        json=payload,
        headers={
            "Authorization": "Bearer {}".format(token["access_token"]),
            "Content-Type": "application/json",
        },
    )
