# SpotiGit

SpotiGit is a tool that allows you to stream music directly on GitHub!

## Installation

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Configure `setup.py`.
3. Run `python main.py`.

## Configuration in `setup.py`

### GITHUB_TOKEN

To obtain a personal access token for GitHub, follow these steps:

1. Log in to your GitHub account.
2. Click on your profile avatar in the top right corner and select "Settings".
3. In the side menu, choose "Developer settings", then "Personal access tokens", and finally "Fine-grained tokens".
4. Click on the "Generate new token" button.
5. Select the necessary access rights for your token. Please note that the more permissions you grant, the more capabilities your token will have, so choose only the permissions that are truly necessary for your project. After selecting permissions, click on the "Generate token" button.
6. Copy the generated token to a secure location as it will not be displayed again after you leave the page.

Remember that the token grants access to your GitHub account, so be cautious and do not share it with third parties. It is also advisable to regularly check and update tokens if they are no longer needed or if you suspect they may have been compromised.

### SPOTIFY_TOKEN

To obtain a personal access token for Spotify, follow these steps:

1. Go to https://developer.spotify.com/dashboard
2. Click on the "Create App" button.
3. Choose "Web API" for Which API/SDKs are you planning to use? and set Redirect URI to http://localhost:5000/callback
4. After creating the app, go to your created application and click on the "Settings" button.
5. Obtain Client ID and Client Secret from Basic Information and paste them into `setup.py` (SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_ID).
6. Run the `get_api_key_spotify.py` file, and it will output your Spotify Token. Paste the token into `setup.py` SPOTIFY_TOKEN. (http://127.0.0.1:5000)

### Setting up REPO_OWNER, REPO_NAME, FILE_PATH and CONTENT_FIND

1. `REPO_OWNER` = your GitHub username.
2. `REPO_NAME` = the name of your repository.
3. `FILE_PATH` = the name of the file to be edited.
4. `CONTENT_FIND` = "🎵 currently playing:" - the string to be searched in the file where the current song will be inserted.

After configuring, run `python main.py`.

## Contributors

- [Uni](https://github.com/unibtw)

## License

This project is licensed under the [MIT License](LICENSE).