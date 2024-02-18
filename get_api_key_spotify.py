import requests
from flask import Flask, request, redirect
import setup
app = Flask(__name__)


CLIENT_ID = setup.SPOTIFY_CLIENT_ID
CLIENT_SECRET = setup.SPOTIFY_SECRET_ID
REDIRECT_URI = setup.SPOTIFY_REDIRECT_URI


@app.route("/")
def login():
    auth_url = f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=user-read-currently-playing"
    return redirect(auth_url)


@app.route("/callback")
def callback():
    code = request.args.get('code')
    auth_url = "https://accounts.spotify.com/api/token"
    auth_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(auth_url, data=auth_data)
    access_token = response.json()["access_token"]
    print('You are Spotify access token:' + access_token)

if __name__ == "__main__":
    app.run(debug=True)
