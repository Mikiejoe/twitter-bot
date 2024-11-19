import json
from django.shortcuts import redirect
from django.http import JsonResponse, HttpRequest
from .tweet import (
    make_token,
    post_tweet,
    code_challenge,
    auth_url,
    token_url,
    code_verifier,
    client_secret,
)
from .gemini import generate_tweet
from .models import Token


def home(request):
    global twitter
    twitter = make_token()
    authorization_url, state = twitter.authorization_url(
        auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )
    request.session["oauth_state"] = state
    request.session["authorization_url"] = authorization_url
    return redirect(authorization_url)


def callback(request: HttpRequest):
    twitter = make_token()
    code = request.GET.get("code")
    token = twitter.fetch_token(
        token_url=token_url,
        client_secret=client_secret,
        code_verifier=code_verifier,
        code=code,
    )
    st_token = '"{}"'.format(token)
    j_token = json.loads(st_token)
    try:
        token_object, _ = Token.objects.update_or_create(
            name="token",  # Field used for lookup
            defaults={"token": j_token},  # Fields to update or set
        )
        token_object.save()
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=500)
    tweet = generate_tweet()
    payload = {"text": f"{tweet}"}
    response = post_tweet(payload, token).json()
    return JsonResponse(response)
